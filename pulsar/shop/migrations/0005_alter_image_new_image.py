# Generated by Django 3.2.16 on 2022-12-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20221214_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='new_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images_webp/', verbose_name='Изображение товара'),
        ),
    ]
