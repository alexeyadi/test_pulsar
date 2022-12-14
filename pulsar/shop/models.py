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
    # images = models.ImageField(verbose_name='Изображение товара',
    #                    upload_to=image_folder,
    #                    null=True,
    #                    blank=True)
    images = models.ForeignKey('Image',
                               verbose_name='Изображение товара',
                               related_name='products',
                               on_delete=models.PROTECT,
                               null=True,
                               blank=True)
    # id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Изображение товара',
                              upload_to='media/images/',
                              null=True,
                              blank=True)
    primary_format = models.CharField(max_length=25,
                                      null=True,
                                      blank=True)
    old_image = models.ImageField(verbose_name='Старое изображение товара',
                                  upload_to='media/images/',
                                  null=True,
                                  blank=True)

    # def save(self, *args, **kwargs):
    #     print(self.image.file)
    #     if self.image:
    #         with Pillow.open(self.image.file) as img:
    #             self.primary_format = img.format
    #             buffer1 = BytesIO()
                
    #             self.old_image.file = deepcopy(self.image.file)
    #             self.image.file = img.save(buffer1, format='WEBP')
    #     super().save(*args, **kwargs)


# class ImageProduct(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     image = models.ForeignKey(Image, on_delete=models.CASCADE)
