from .models import City, DeliveryBody, Delivery
import requests
import datetime
from bs4 import BeautifulSoup


def get_delivery_data():
    try:
        url = 'https://sistemavl.ru/tarif'
        response = requests.get(url)
        bs = BeautifulSoup(response.text, "lxml")
        table = bs.findAll('tr', 'tabrow')

        car_types = []

        for col in table[0]:
            header = col.get_text(strip=True).capitalize()
            if header != 'Направление' and header != 'Расстояние от владивостока, км' and header != 'Время в пути , до, в сутках' and header != '':
                _, _ = DeliveryBody.objects.get_or_create(name=header)
                car_types.append(header)
                print('---')
                print(header)

        for i in range(1, len(table)):
            colls = table[i].find_all('td')
            city = colls[0].get_text(strip=True)

            if (city == 'Нижний -Н'):
                city = 'Нижний-Новгород'
            elif (city == 'С-Петербург'):
                city = 'Санкт-Петербург'
            elif (city == 'Н-Челны'):
                city = 'Набережные-Челны'

            if city != '':
                city_obj, _ = City.objects.get_or_create(name=city)

            for j in range(1, len(colls) - 2):
                price = colls[j].get_text(strip=True)

                body_type_name = car_types[j - 1]
                body_type_obj = DeliveryBody.objects.get(name=body_type_name)

                _, _ = Delivery.objects.get_or_create(
                    city=city_obj,
                    body_type=body_type_obj,
                    price=price
                )
    except Exception as e:
        print(e)
