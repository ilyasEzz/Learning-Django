from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listings(models.Model):
    realtor = models.ForeignKey(
        Realtor, on_delete=models.DO_NOTHING, verbose_name="Специалист")
    title = models.CharField(max_length=200,  verbose_name="Названия")
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)

    # "blank=True" => optional, not required
    description = models.TextField(blank=True, verbose_name="описание")
    price = models.IntegerField(verbose_name="цена")
    bedrooms = models.IntegerField(blank=True)
    bathrooms = models.IntegerField(blank=True)
    garage = models.IntegerField(default=0, blank=True)
    square_metre = models.IntegerField(blank=True)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, blank=True)

    photo_main = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True,  verbose_name="основное изображение")
    photo_1 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True,  verbose_name="изображение 1")
    photo_2 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="изображение 2")
    photo_3 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="изображение 3")
    photo_4 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="изображение 4")
    photo_5 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="изображение 5")
    photo_6 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="изображение 6")
    is_published = models.BooleanField(default=True, verbose_name="отображать")
    list_date = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name=" дата")

    @property
    def get_comments(self):
        return self.comments.all()

    # display the title in the  admin table

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "объявления"
