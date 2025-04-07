from django.db import models


class MainBlock(models.Model):
    rate_clients = models.CharField(max_length=50, verbose_name='Рейтинг клиентов')
    year = models.IntegerField(verbose_name='Лет на рынке')
    cnt_car = models.CharField(max_length=100, verbose_name='Авто привезли')
    min_day_delivery = models.CharField(max_length=100, verbose_name='Минимальный срок доставки')

    class Meta:
        verbose_name = 'Главный экран'
        verbose_name_plural = 'Главный экран'

    def __str__(self):
        return 'Данные главного экрана'


class StagesOfWork(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Этапы работы'
        verbose_name_plural = 'Этапы работы'

    def __str__(self):
        return self.name


class Contact(models.Model):
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')
    email = models.CharField(max_length=50, verbose_name='Email')
    address = models.TextField(verbose_name='Адрес')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.phone} | {self.email}'


class CommandCompany(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИ члена команды')
    position = models.CharField(max_length=50, verbose_name='Должность')
    image_user = models.ImageField(upload_to='users')

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команда'

    def __str__(self):
        return f'{self.name} | {self.position}'

