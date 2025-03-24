from youtube.tasks import get_shorts_videos_data
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Загрузка shorts с ютуб'

    def handle(self, *args, **kwargs):
        print('Загрузка началась')
        get_shorts_videos_data()
        print('Загрузка завершилась')
