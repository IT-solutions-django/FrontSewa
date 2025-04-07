from django.db import models


class FeedBack(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение', null=True, blank=True)
    city_delivery = models.CharField(max_length=100, verbose_name='Город доставки', null=True, blank=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.phone} | {self.message}'


