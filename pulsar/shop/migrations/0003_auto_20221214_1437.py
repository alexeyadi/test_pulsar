# Generated by Django 3.2.16 on 2022-12-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20221214_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='old_image',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/', verbose_name='Изображение товара'),
        ),
    ]
