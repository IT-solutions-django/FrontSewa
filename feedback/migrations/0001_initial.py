# Generated by Django 5.1.7 on 2025-04-06 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
                ('city_delivery', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город доставки')),
            ],
        ),
    ]
