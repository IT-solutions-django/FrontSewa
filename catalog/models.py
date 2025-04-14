from django.db import models


COUNTRY_CHOICES = (
    ('Япония', "Япония"),
    ('Китай', "Китай"),
    ('Корея', "Корея"),
    ('Европа', "Европа"),
)


class CarPromoBlock(models.Model):
    country = models.CharField(max_length=100, verbose_name='Страна', choices=COUNTRY_CHOICES)
    name = models.TextField(verbose_name='Заголовок к авто')
    price = models.CharField(max_length=50, verbose_name='Цена авто')
    old_price = models.CharField(max_length=50, verbose_name='Старая цена авто')
    image_car = models.ImageField(upload_to='promo_car', verbose_name='Фото авто')

    class Meta:
        verbose_name = "Авто для промо блока"
        verbose_name_plural = "Авто для промо блока"

    def __str__(self):
        return f"{self.name}"


class ExclusiveOfferCarPhoto(models.Model):
    image = models.ImageField(upload_to='promo_car')

    class Meta:
        verbose_name = "Фото для эксклюзивного предложения авто"
        verbose_name_plural = "Фото для эксклюзивного предложения авто"

    def __str__(self):
        return f"{self.image.name}"


class ExclusiveOfferCar(models.Model):
    name = models.TextField(verbose_name='Название авто', null=True, blank=True)
    eng_v = models.CharField(max_length=50, verbose_name='Объем двигателя', null=True, blank=True)
    engine = models.CharField(max_length=100, verbose_name='Тип двигателя', null=True, blank=True)
    power_volume = models.CharField(max_length=100, verbose_name='Мощность двигателя', null=True, blank=True)
    drive = models.CharField(max_length=100, verbose_name='Тип привода', null=True, blank=True)
    year = models.CharField(max_length=50, verbose_name='Год', null=True, blank=True)
    mileage = models.CharField(max_length=50, verbose_name='Пробег', null=True, blank=True)
    color = models.CharField(max_length=100, verbose_name='Цвет', null=True, blank=True)
    price = models.CharField(max_length=100, verbose_name='Цена', null=True, blank=True)
    percent_price = models.PositiveIntegerField(default=5, verbose_name='Процент', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Активна', null=True, blank=True)
    date = models.DateField(verbose_name='Дата добавления', null=True, blank=True, auto_now_add=True)
    images = models.ManyToManyField(ExclusiveOfferCarPhoto, null=True, blank=True)

    class Meta:
        verbose_name = "Эксклюзивное предложение авто"
        verbose_name_plural = "Эксклюзивное предложение авто"

    def __str__(self):
        return f"{self.name}"

