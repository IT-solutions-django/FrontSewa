# Generated by Django 5.1.7 on 2025-04-14 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExclusiveOfferCarPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='promo_car')),
            ],
            options={
                'verbose_name': 'Фото для эксклюзивного предложения авто',
                'verbose_name_plural': 'Фото для эксклюзивного предложения авто',
            },
        ),
        migrations.CreateModel(
            name='ExclusiveOfferCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Название авто')),
                ('eng_v', models.CharField(blank=True, max_length=50, null=True, verbose_name='Объем двигателя')),
                ('engine', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип двигателя')),
                ('power_volume', models.CharField(blank=True, max_length=100, null=True, verbose_name='Мощность двигателя')),
                ('drive', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип привода')),
                ('year', models.CharField(blank=True, max_length=50, null=True, verbose_name='Год')),
                ('mileage', models.CharField(blank=True, max_length=50, null=True, verbose_name='Пробег')),
                ('color', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет')),
                ('price', models.CharField(blank=True, max_length=100, null=True, verbose_name='Цена')),
                ('percent_price', models.PositiveIntegerField(blank=True, default=5, null=True, verbose_name='Процент')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Активна')),
                ('date', models.DateField(auto_now_add=True, null=True, verbose_name='Дата добавления')),
                ('images', models.ManyToManyField(blank=True, null=True, to='catalog.exclusiveoffercarphoto')),
            ],
            options={
                'verbose_name': 'Эксклюзивное предложение авто',
                'verbose_name_plural': 'Эксклюзивное предложение авто',
            },
        ),
    ]
