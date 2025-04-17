from django.shortcuts import render
from collections import defaultdict
import requests
from django.http import JsonResponse
import json
from youtube.models import Video, ShortVideo, ReviewVideo
from delivery.models import City, DeliveryBody, Delivery
from information.models import MainBlock, StagesOfWork, Contact
from .models import CarPromoBlock, ExclusiveOfferCar
from urllib.parse import unquote
import random
from django.utils import timezone
from datetime import timedelta


def send_order(request):
    body_param = json.loads(request.body)

    city_name = body_param.get('city')
    car_type_name = body_param.get('carType')

    car_type_delivery = DeliveryBody.objects.filter(name=car_type_name).first()
    if not car_type_delivery:
        return JsonResponse({"error": "Такой тип кузова не найден"}, status=400)

    city_delivery = City.objects.filter(name=city_name).first()
    if not city_delivery:
        return JsonResponse({"error": "Такой город не найден"}, status=400)

    delivery_data = Delivery.objects.filter(city=city_delivery, body_type=car_type_delivery).first()

    if not delivery_data:
        return JsonResponse({"error": "Доставка не найдена"}, status=404)

    return JsonResponse({"price_delivery": delivery_data.price}, status=200)


def get_main_cars(params):
    url = "http://193.164.149.51/cars/get-main-cars/"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        popular_korea, popular_japan, popular_china, popular_europe = response.json()['popular_cars_korea'], response.json()['popular_cars_japan'], response.json()['popular_cars_china'], response.json()['popular_cars_europe']
        return popular_korea, popular_japan, popular_china, popular_europe

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


def home(request):
    videos = Video.objects.all()
    shorts = ShortVideo.objects.all()
    videos_review = ReviewVideo.objects.all()
    city_delivery = City.objects.all()
    body_delivery = DeliveryBody.objects.all()

    info_main = MainBlock.objects.all().first()

    stages_work = StagesOfWork.objects.all()

    contact = Contact.objects.all().first()

    params = {
        'ip': '94.241.142.204'
    }

    popular_korea, popular_japan, popular_china, popular_europe = get_main_cars(params)

    return render(request, 'home.html', {
        'videos': videos,
        'shorts': shorts,
        'videos_review': videos_review,
        'city_delivery': city_delivery,
        'body_delivery': body_delivery,
        'info_main': info_main,
        'stages_work': stages_work,
        'contact': contact,
        'popular_korea': popular_korea,
        'popular_japan': popular_japan,
        'popular_china': popular_china,
        'popular_europe': popular_europe
    })


def about(request):
    videos = Video.objects.all()

    shorts = ShortVideo.objects.all()

    info_main = MainBlock.objects.all().first()

    contact = Contact.objects.all().first()

    return render(request, 'about.html', {'videos': videos, 'info_main': info_main, 'contact': contact, 'shorts': shorts})


def get_brands_from_api(params):
    url = "http://193.164.149.51/cars/get-brands/"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


def get_cars_from_api(params):
    url = "http://193.164.149.51/cars/get-cars"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data, total_pages, curr_page = response.json()['cars'], response.json()['total_pages'], response.json()[
            'current_page']
        return data, total_pages, curr_page

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


def get_models_from_api(request):
    params = {
        'ip': request.GET.get('ip'),
        'brand': request.GET.get('brand')
    }

    url = "http://193.164.149.51/cars/get-models/"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data_model = response.json()

        grouped_data_model = defaultdict(set)

        for key, value in data_model:
            normalized_value = value.title()
            grouped_data_model[normalized_value].add(key)

        models = {", ".join(keys): value for value, keys in grouped_data_model.items()}

        return JsonResponse(models)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


def get_all_models_from_api(ip_addr):
    params = {
        'ip': ip_addr,
    }

    url = "http://193.164.149.51/cars/get-all-models/"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data_model = response.json()

        grouped_data_model = defaultdict(set)

        for key, value in data_model:
            normalized_value = value.title()
            grouped_data_model[normalized_value].add(key)

        models = {", ".join(keys): value for value, keys in grouped_data_model.items()}

        return models

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


def catalog(request, country=None):
    params = {
        'ip': '94.241.142.204'
    }

    if country:
        params['country'] = country

    if request.GET:
        brand = request.GET.get('brand')
        if brand:
            params['brand'] = brand
        drive = request.GET.get('drive')
        if drive:
            params['drive'] = drive
        transmission = request.GET.get('transmission')
        if transmission:
            params['transmission'] = transmission
        engine_volume_from = request.GET.get('engine_volume_from')
        if engine_volume_from:
            params['engine_volume_from'] = engine_volume_from
        engine_volume_to = request.GET.get('engine_volume_to')
        if engine_volume_to:
            params['engine_volume_to'] = engine_volume_to
        model = request.GET.get('model')
        if model:
            params['model'] = model
        year_from = request.GET.get('year_from')
        if year_from:
            params['year_from'] = year_from
        year_to = request.GET.get('year_to')
        if year_to:
            params['year_to'] = year_to
        car_fuel = request.GET.get('car_fuel')
        if car_fuel:
            params['car_fuel'] = car_fuel
        car_type = request.GET.get('car_type')
        if car_type:
            params['car_type'] = car_type
        price_from = request.GET.get('price_from')
        if price_from:
            price_from_params = price_from.replace("\xa0", "")
            params['price_from'] = price_from_params
        price_to = request.GET.get('price_to')
        if price_to:
            price_to_format = price_to.replace("\xa0", "")
            params['price_to'] = price_to_format

        mileage_from = request.GET.get('mileage_from')
        if mileage_from:
            params['mileage_from'] = mileage_from
        mileage_to = request.GET.get('mileage_to')
        if mileage_to:
            params['mileage_to'] = mileage_to
        auction = request.GET.get('auction')
        if auction:
            params['auction'] = auction
        color = request.GET.get('color')
        if color:
            params['color'] = color
        order = request.GET.get('order')
        if order:
            params['order'] = order
        page = request.GET.get('page')
        if page:
            params['page'] = page

    data_cars, total_pages, current_page = get_cars_from_api(params)

    min_page = max(current_page - 2, 2)
    max_page = min(current_page + 2, total_pages - 1)
    page_range = list(range(min_page, max_page + 1))

    params_for_brand = {
        'ip': '94.241.142.204',
        'country': country
    }
    data_brand = get_brands_from_api(params_for_brand)

    data_model = [

    ]

    data_drive = {
        ('4WD', 'AWD', '4륜', 'Полный привод'): 'Полный привод',
        ('후륜 RR', '후륜', 'Задний привод', 'RR', '후륜 미드쉽'): 'Задний привод',
        ('전륜', 'Передний привод', 'FF', '전륜 FF'): 'Передний привод'
    }

    data_transmission = {
        ('자동', 'CVT', '세미오토', '기타', '오토', 'Автомат'): 'Автомат',
        ('수동', 'Механика'): 'Механика'
    }

    data_engine_volume = {int(value * 1000): f'{value} л' for value in [round(x * 0.1, 1) for x in range(1, 61)]}

    data_year = {value: value for value in range(2008, 2026)}

    data_car_fuel = {
        ('전기', 'Электро'): 'Электро',
        ('LPG+가솔린', '디젤+전기', '수소', '가솔린+전기', 'LPG+전기', 'LPG', '가솔린+LPG', '수소+전기', '기타', '가솔린/LPG겸용', '가솔린 하이브리드',
         '디젤 하이브리드', 'Гибрид'): 'Гибрид',
        ('디젤', 'Дизель'): 'Дизель',
        ('가솔린', 'Бензин'): 'Бензин'
    }

    data_car_type = {
        ('세단', '중형차', '대형차', '준중형차', '소형차', '경차', ' 기타'): 'Седан',
        ('해치백',): 'Хэтчбек',
        ('쿠페', '스포츠카', '컨버터블'): 'Купе',
        ('밴(승합)', '승합차', '왜건'): 'Минивэн',
        ('RV', 'SUV', '특장차'): 'Внедорожник',
        ('픽업(화물)', '화물차'): 'Пикап'
    }

    data_mileage = {value: f'{value:,} км'.replace(',', ' ') for value in range(10000, 200000 + 1, 10000)}

    grouped_data_brand = defaultdict(set)

    grouped_data_model = defaultdict(set)

    for key, value in data_brand:
        normalized_value = value.title()
        grouped_data_brand[normalized_value].add(key)

    for key, value in data_model:
        normalized_value = value.title()
        grouped_data_model[normalized_value].add(key)

    brands = {tuple(keys): value for value, keys in grouped_data_brand.items()}

    models = {tuple(keys): value for value, keys in grouped_data_model.items()}

    brand_map = {"{}".format(",".join(keys)): value for keys, value in brands.items()}

    # model_map = get_all_models_from_api('94.241.142.204')

    drive_map = {"{}".format(",".join(keys)): value for keys, value in data_drive.items()}

    transmission_map = {"{}".format(",".join(keys)): value for keys, value in data_transmission.items()}

    car_fuel_map = {"{}".format(",".join(keys)): value for keys, value in data_car_fuel.items()}

    car_type_map = {"{}".format(",".join(keys)): value for keys, value in data_car_type.items()}

    if country == 'Китай':
        country_temp = 'Китая'
    elif country == 'Корея':
        country_temp = 'Кореи'
    elif country == 'Япония':
        country_temp = 'Японии'
    elif country == 'Европа':
        country_temp = 'Европы'
    else:
        country_temp = ''

    city_delivery = City.objects.all()
    body_delivery = DeliveryBody.objects.all()

    contact = Contact.objects.all().first()

    seven_days_ago = timezone.now().date() - timedelta(days=7)

    promo_car = ExclusiveOfferCar.objects.prefetch_related('images').filter(is_active=True)
    if promo_car:
        promo_car_list = list(promo_car)
        random.shuffle(promo_car_list)
        random_promo_cars = promo_car_list[0]
    else:
        random_promo_cars = None

    return render(
        request, 'catalog.html',
        {
            'result': brands,
            'brand_map': brand_map,
            'models': models,
            'drive': data_drive,
            'drive_map': drive_map,
            'transmission': data_transmission,
            'transmission_map': transmission_map,
            'engine_volume': data_engine_volume,
            'year': data_year,
            'car_fuel': data_car_fuel,
            'car_fuel_map': car_fuel_map,
            'car_type': data_car_type,
            'car_type_map': car_type_map,
            'mileage': data_mileage,
            'cars': data_cars,
            'total_pages': total_pages,
            'current_page': current_page,
            'page_range': page_range,
            'country_temp': country_temp,
            'city_delivery': city_delivery,
            'body_delivery': body_delivery,
            'contact': contact,
            'promo_car': random_promo_cars
        }
    )


def get_car_from_api(car_id):
    params = {
        'ip': '94.241.142.204',
        'id': car_id
    }
    url = "http://193.164.149.51/cars/get-car/"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data, popular_cars, details_price_car = response.json()['car'], response.json()['popular_cars'], response.json()['detailed_calculation']
        return data, popular_cars, details_price_car

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


def translate_brand_car_card(car_brand):
    params = {
        'ip': '94.241.142.204',
        'brand': car_brand
    }

    url = "http://193.164.149.51/cars/get-ru-brand/"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()['ru_brand']
        return data

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


def translate_model_car_card(car_model):
    params = {
        'ip': '94.241.142.204',
        'model': car_model
    }

    url = "http://193.164.149.51/cars/get-ru-model/"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()['ru_model']
        return data

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


def car(request, id_car):
    data_car, popular_cars, details_price_car = get_car_from_api(id_car)

    city_delivery = City.objects.all()
    body_delivery = DeliveryBody.objects.all()

    country = data_car.get('country')

    if country == 'Китай':
        country_temp = 'Китая'
        country_path = 'china'
    elif country == 'Корея':
        country_temp = 'Кореи'
        country_path = 'korea'
    elif country == 'Япония':
        country_temp = 'Японии'
        country_path = 'japan'
    elif country == 'Европа':
        country_temp = 'Европы'
        country_path = 'europe'
    else:
        country_temp = ''
        country_path = '#'

    info_main = MainBlock.objects.all().first()

    stages_work = StagesOfWork.objects.all()

    contact = Contact.objects.all().first()

    if details_price_car:
        poshlina = float(details_price_car["toll"]) + float(details_price_car["yts"]) + float(details_price_car["tof"])
    else:
        poshlina = 0

    return render(request, 'card.html', {'car': data_car, 'city_delivery': city_delivery, 'body_delivery': body_delivery, 'popular_cars': popular_cars, 'country_temp': country_temp, 'country_path': country_path, 'details_price_car': details_price_car, 'info_main': info_main, 'stages_work': stages_work, 'contact': contact, 'poshlina': poshlina})


def get_promo_car_card(request, id_car):
    promo_car = ExclusiveOfferCar.objects.prefetch_related('images').get(id=id_car)

    city_delivery = City.objects.all()
    body_delivery = DeliveryBody.objects.all()

    info_main = MainBlock.objects.all().first()

    stages_work = StagesOfWork.objects.all()

    contact = Contact.objects.all().first()

    return render(request, 'promo_card.html', {
        'car': promo_car,
        'city_delivery': city_delivery,
        'body_delivery': body_delivery,
        'info_main': info_main,
        'stages_work': stages_work,
        'contact': contact,
    })

