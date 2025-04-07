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
