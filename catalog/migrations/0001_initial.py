# Generated by Django 5.1.7 on 2025-04-06 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarPromoBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('Япония', 'Япония'), ('Китай', 'Китай'), ('Корея', 'Корея'), ('Европа', 'Европа')], max_length=100, verbose_name='Страна')),
                ('name', models.TextField(verbose_name='Заголовок к авто')),
                ('price', models.CharField(max_length=50, verbose_name='Цена авто')),
                ('old_price', models.CharField(max_length=50, verbose_name='Старая цена авто')),
                ('image_car', models.ImageField(upload_to='promo_car', verbose_name='Фото авто')),
            ],
            options={
                'verbose_name': 'Авто для промо блока',
                'verbose_name_plural': 'Авто для промо блока',
            },
        ),
    ]
