# Generated by Django 3.2.16 on 2022-12-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_image_new_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='new_image',
            field=models.ImageField(blank=True, null=True, upload_to='images_webp/', verbose_name='Изображение товара'),
        ),
        migrations.AlterField(
            model_name='image',
            name='old_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение товара'),
        ),
    ]
