from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=200, verbose_name = "ФИО")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name = "фото")
    description = models.TextField(blank=True, verbose_name = "описание")
    phone = models.CharField(max_length=20, verbose_name = "номер телефона")
    email = models.CharField(max_length=50, verbose_name = "почта")
    is_mvp = models.BooleanField(default=False,  verbose_name = "топ специалист")
    hire_date = models.DateField(default=datetime.now, blank=True,  verbose_name = "дата найма")

    # display the title in the  admin table
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "специалист" 
        verbose_name_plural = "специалисты"
