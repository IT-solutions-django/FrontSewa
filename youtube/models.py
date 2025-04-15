from django.db import models
from django.utils.translation import gettext_lazy as _
import os
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from urllib.parse import urlparse


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
    preview_img = models.ImageField(upload_to='video', null=True, blank=True, verbose_name='Фото превью видео')
    video_id = models.CharField(max_length=100, verbose_name='Айди видео', null=True)
    date_published = models.DateField(verbose_name=_("Дата публикации видео ролика"))

    class Meta:
        verbose_name = _('Видео')
        verbose_name_plural = _('Видео')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.preview and not self.preview_img:
            try:

                response = requests.get(self.preview, stream=True)
                response.raise_for_status()

                img_name = os.path.basename(urlparse(self.preview).path)

                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(response.content)
                img_temp.flush()

                self.preview_img.save(img_name, File(img_temp), save=False)

            except Exception as e:
                print(f"Ошибка загрузки изображения: {e}")

        super().save(*args, **kwargs)


class ShortVideo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название короткого видео')
    link = models.TextField(verbose_name='Ссылка на короткое видео')
    preview = models.TextField(verbose_name='Превью короткого видео')
    preview_img = models.ImageField(verbose_name='Превью видео', upload_to='video', null=True, blank=True)
    video_path = models.TextField(verbose_name='Путь к видео', default='zero', null=True)
    video_id = models.CharField(max_length=100, verbose_name='Айди видео', null=True)
    date_published = models.DateField(verbose_name=_("Дата публикации видео ролика"))

    class Meta:
        verbose_name = _('Короткое видео')
        verbose_name_plural = _('Короткое видео')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.preview and not self.preview_img:
            try:

                response = requests.get(self.preview, stream=True)
                response.raise_for_status()

                img_name = os.path.basename(urlparse(self.preview).path)

                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(response.content)
                img_temp.flush()

                self.preview_img.save(img_name, File(img_temp), save=False)

            except Exception as e:
                print(f"Ошибка загрузки изображения: {e}")

        super().save(*args, **kwargs)


class ReviewVideo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название видео')
    link = models.TextField(verbose_name='Ссылка на видео')
    preview = models.TextField(verbose_name='Превью видео')
    preview_img = models.ImageField(verbose_name='Фото превью видео', upload_to='video')
    video_id = models.CharField(max_length=100, verbose_name='Айди видео', null=True)
    date_published = models.DateField(verbose_name=_("Дата публикации видео ролика"))

    class Meta:
        verbose_name = _('Видео отзывы')
        verbose_name_plural = _('Видео отзывы')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.preview and not self.preview_img:
            try:

                response = requests.get(self.preview, stream=True)
                response.raise_for_status()

                img_name = os.path.basename(urlparse(self.preview).path)

                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(response.content)
                img_temp.flush()

                self.preview_img.save(img_name, File(img_temp), save=False)

            except Exception as e:
                print(f"Ошибка загрузки изображения: {e}")

        super().save(*args, **kwargs)
