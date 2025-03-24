from youtube.tasks import get_videos
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Загрузка видео с ютуб'

    def handle(self, *args, **kwargs):
        print('Загрузка началась')
        get_videos()
        print('Загрузка завершилась')
