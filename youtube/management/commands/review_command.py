from youtube.tasks import get_review_videos_data
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Загрузка reviews с ютуб'

    def handle(self, *args, **kwargs):
        print('Загрузка началась')
        get_review_videos_data()
        print('Загрузка завершилась')
