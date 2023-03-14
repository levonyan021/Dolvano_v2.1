from django.db import models
from django.conf import settings
from django.urls import reverse
import uuid


class Product(models.Model):
    rubric = models.ForeignKey("Rubric", on_delete=models.CASCADE, blank=True, null=True, verbose_name='Ռուբրիկա')
    popular = models.BooleanField(null=True, blank=True, default=False)
    name = models.CharField(max_length=200, verbose_name='Անուն')
    product_code = models.CharField(max_length=200, verbose_name='Կոդ')
    color = models.ForeignKey('Color', on_delete=models.CASCADE, verbose_name="Գույն", null=True, blank=True)
    mini_description = models.TextField(verbose_name='Փոքր նկարագիր')
    card_photo = models.ImageField(upload_to='clock_photos/', verbose_name='Քարտի նկար 220x220')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Գինը')
    background_photo = models.ImageField(upload_to='clock_photos/', verbose_name='Բաների նկար')
    info_image_1 = models.ImageField(upload_to='clock_photos/', verbose_name='Ինֆո 1 նկար')
    info_header_1 = models.TextField(verbose_name='Ինֆո 1 վերնագգիր ', null=True, blank=True)
    info_description_1 = models.TextField(verbose_name='Ինֆո 1 ')
    info_image_2 = models.ImageField(upload_to='clock_photos/', verbose_name='Ինֆո 2 նկար')
    info_header_2 = models.TextField(verbose_name='Ինֆո 2 վերնագգիր ', null=True, blank=True)
    info_description_2 = models.TextField(verbose_name='Ինֆո 2 ',)
    info_image_3 = models.ImageField(upload_to='clock_photos/', verbose_name='Ինֆո 3 նկար')
    info_header_3 = models.TextField(verbose_name='Ինֆո 3 վերնագգիր', null=True, blank=True)
    info_description_3 = models.TextField(verbose_name='Ինֆո 3 ')
    slider_photo_1 = models.ImageField(upload_to='clock_photos/', verbose_name='սլայդի նկար 1')
    slider_photo_2 = models.ImageField(upload_to='clock_photos/', verbose_name='սլայդի նկար 2')
    slider_photo_3 = models.ImageField(upload_to='clock_photos/', verbose_name='սլայդի նկար 3')
    slider_photo_4 = models.ImageField(upload_to='clock_photos/', verbose_name='սլայդի նկար 4')
    slider_photo_5 = models.ImageField(upload_to='clock_photos/', verbose_name='սլայդի նկար 5')
    youtube_link = models.TextField(verbose_name='Youtube Link', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Ամսաթիվ')

    def __str__(self):
        return self.name


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Անվանում')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Ռուբրիկաներ'
        verbose_name = 'Ռուբրիկա'
        ordering = ['name']



class Information(models.Model):
    image1 = models.ImageField(upload_to='info/')
    description1 = models.TextField()
    image2 = models.ImageField(upload_to='info/')
    description2 = models.TextField()

    def __str__(self):
        return self.description1
    

class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=7)
    def __str__(self):
        return self.name

class ClockColor(models.Model):
    clock = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)