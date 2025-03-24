from delivery.tasks import get_delivery_data
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Парсинг данных о доставке авто'

    def handle(self, *args, **kwargs):
        print('Парсинг начался')
        get_delivery_data()
        print('Парсинг завершился')
