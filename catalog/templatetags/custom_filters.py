from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, key)


@register.filter
def get_item_int(dictionary, key):
    return dictionary.get(int(key), key)


@register.filter
def format_number(value):
    try:
        value = int(value)
        return "{:,.0f}".format(value).replace(",", " ")
    except (ValueError, TypeError):
        return value


@register.filter
def format_price(value):
    try:
        return "{:,.0f}".format(int(value)).replace(",", " ")
    except (ValueError, TypeError):
        return value


@register.filter
def cc_to_liters(value):
    try:
        return round(int(value) / 1000, 1)
    except (ValueError, TypeError):
        return value


@register.filter
def translate_transmission(value):
    data_transmission = {
        ('자동', 'CVT', '세미오토', '기타', '오토', 'Автомат'): 'Автомат',
        ('수동', 'Механика'): 'Механика'
    }

    for key, translated_value in data_transmission.items():
        if value in key:
            return translated_value
    return value


@register.filter
def translate_engine(value):
    data_car_fuel = {
        ('전기', 'Электро'): 'Электро',
        ('LPG+가솔린', '디젤+전기', '수소', '가솔린+전기', 'LPG+전기', 'LPG', '가솔린+LPG', '수소+전기', '기타', '가솔린/LPG겸용', '가솔린 하이브리드',
         '디젤 하이브리드', 'Гибрид'): 'Гибрид',
        ('디젤', 'Дизель'): 'Дизель',
        ('가솔린', 'Бензин'): 'Бензин'
    }

    for key, translated_value in data_car_fuel.items():
        if value in key:
            return translated_value
    return value


@register.filter
def translate_drive(value):
    data_drive = {
        ('4WD', 'AWD', '4륜', 'Полный привод'): 'Полный привод',
        ('후륜 RR', '후륜', 'Задний привод', 'RR', '후륜 미드쉽', '후륜 '): 'Задний привод',
        ('전륜', 'Передний привод', 'FF', '전륜 FF'): 'Передний привод'
    }

    for key, translated_value in data_drive.items():
        if value in key:
            return translated_value
    return value


@register.filter
def translate_brand(dictionary, value):
    for key, translated_value in dictionary.items():
        if value in key:
            return translated_value
    return value


@register.filter
def translate_model(dictionary, value):
    for key, translated_value in dictionary.items():
        list_key = list(map(lambda s: s.strip(), key.split(',')))
        for string in list_key:
            if value == string:
                return translated_value

    return value


@register.filter
def filter_photo(value):
    new_url_photo = value[:len(value) - 3] + '&w=320'
    return new_url_photo


@register.filter
def filter_photo_card_car(value):
    new_url_photo = value[:len(value) - 3]

    return new_url_photo


@register.filter
def translate_body_type(value):
    data_car_type = {
        ('세단', '중형차', '대형차', '준중형차', '소형차', '경차', '기타'): 'Седан',
        ('해치백',): 'Хэтчбек',
        ('쿠페', '스포츠카', '컨버터블'): 'Купе',
        ('밴(승합)', '승합차', '왜건'): 'Минивэн',
        ('RV', 'SUV', '특장차'): 'Внедорожник',
        ('픽업(화물)', '화물차'): 'Пикап'
    }

    for key, translated_value in data_car_type.items():
        if value in key:
            return translated_value
    return value


@register.filter
def filter_price_korea(value):
    return value + '0000'


@register.filter
def truncate_decimal(value, digits=3):
    try:
        return round(float(value), digits)
    except (ValueError, TypeError):
        return value


@register.filter
def add_percent(value, percent):
    try:
        value = value.replace(' ', '')
        value = int(value)
        percent = int(percent)
        return int(value * (1 + percent / 100))
    except (ValueError, TypeError):
        return value


@register.filter
def cnt_start(value, cnt):
    try:
        cnt = int(round(float(cnt)))
        return [i for i in range(cnt)]
    except Exception:
        return [1, 2, 3, 4]
