from django.db import models
from django.utils.translation import gettext_lazy as _


class Youtube(models.Model):
    videos_url = models.TextField(verbose_name='Ссылка на канал', null=False, blank=False)
    shorts_url = models.TextField(verbose_name='Ссылка на плейлист с шортсами', null=False, blank=False)
    review_url = models.TextField(verbose_name='Ссылка на плейлист с отзывами', null=False, blank=False)
    videos_count = models.IntegerField(verbose_name='Количество выгружаемых видео', null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = _('Ютуб')

    def __str__(self):
        return f'Ютуб от {self.updated_at}'


class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название видео')
    link = models.TextField(verbose_name='Ссылка на видео')
    preview = models.TextField(verbose_name='Превью видео')
    video_id = models.CharField(max_length=100, verbose_name='Айди видео', null=True)
    date_published = models.DateField(verbose_name=_("Дата публикации видео ролика"))

    class Meta:
        verbose_name = _('Видео')
        verbose_name_plural = _('Видео')

    def __str__(self):
        return self.title


class ShortVideo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название короткого видео')
    link = models.TextField(verbose_name='Ссылка на короткое видео')
    preview = models.TextField(verbose_name='Превью короткого видео')
    video_path = models.TextField(verbose_name='Путь к видео', default='zero', null=True)
    video_id = models.CharField(max_length=100, verbose_name='Айди видео', null=True)
    date_published = models.DateField(verbose_name=_("Дата публикации видео ролика"))

    class Meta:
        verbose_name = _('Короткое видео')
        verbose_name_plural = _('Короткое видео')

    def __str__(self):
        return self.title
    