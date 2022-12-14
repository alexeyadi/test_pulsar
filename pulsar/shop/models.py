from django.db import models
from io import BytesIO

from PIL import Image as Pillow
from copy import deepcopy


class Product(models.Model):
    IN_STOCK = 'В наличии'
    UNDER_THE_ORDER = 'Под заказ'
    EXPECTED = 'Ожидается поступление'
    OUT_OF_STOCK = 'Нет в наличии'
    NOT_PRODUCED = 'Не производится'

    STATUSES = [
        (IN_STOCK, 'В наличии'),
        (UNDER_THE_ORDER, 'Под заказ'),
        (EXPECTED, 'Ожидается поступление'),
        (OUT_OF_STOCK, 'Нет в наличии'),
        (NOT_PRODUCED, 'Не производится')
    ]
    title = models.CharField(verbose_name='Название товара', max_length=255, )
    model_number = models.CharField(verbose_name='Артикул товара',
                                    max_length=255,
                                    unique=True)
    price = models.DecimalField(verbose_name='Цена',
                                max_digits=15,
                                decimal_places=2)
    status = models.CharField(verbose_name='Статус товара',
                              choices=STATUSES,
                              default=IN_STOCK,
                              max_length=25)
    images = models.ForeignKey('Image',
                               verbose_name='Изображение товара',
                               related_name='products',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Image(models.Model):
    old_image = models.ImageField(verbose_name='Изображение товара',
                                  upload_to='images/',
                                  null=True,
                                  blank=True)
    new_image = models.ImageField(verbose_name='Изображение товара',
                                  upload_to='images_webp/',
                                  null=True,
                                  blank=True)
    old_format = models.CharField(max_length=10, null=True, blank=True)
    new_format = models.CharField(max_length=10, null=True, blank=True)

    @property
    def formats(self):
        return self.old_format, self.new_format

    @property
    def path(self):
        return self.old_image.url.rpartition('.')[0]

    def save(self, *args, **kwargs):
        with Pillow.open(self.old_image.file) as img:
            if img.format != 'WEBP' and img.format in ('JPG', 'PNG'):
                buffer = BytesIO()
                img.save(buffer, format='WEBP')
                self.old_format = img.format
                with Pillow.open(buffer) as new_image:
                    self.new_format = new_image.format
                self.new_image.file = buffer
        super().save(*args, **kwargs)
