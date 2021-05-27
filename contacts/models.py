from django.db import models
from datetime import datetime

from django.db.models.aggregates import Sum

from listings.models import Listings

# Create your models here.


class Contact(models.Model):
    listing = models.CharField(max_length=200, verbose_name="услуга")
    listing_id = models.ForeignKey(
        Listings, on_delete=models.CASCADE, related_name='listings', verbose_name="Специалист")
    name = models.CharField(max_length=200, verbose_name="ФИО")
    email = models.CharField(max_length=200, verbose_name="почта")
    phone = models.CharField(max_length=200, verbose_name="номер телефона")
    message = models.TextField(blank=True, verbose_name='сообщение')
    contact_date = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name='дата')
    user_id = models.IntegerField(verbose_name="пользователь")
    status = models.BooleanField(default=False, verbose_name="статус")

    def __str__(self):
        return self.name

    @property
    def get_listings_price(self):
        return self.listings.aggregate(Sum('price'))

    @property
    def get_listings(self):
        return self.listings.all()

    class Meta:
        verbose_name_plural = "Абонтменты"
        verbose_name = "Абонтмент"


class Comment(models.Model):
    listings = models.ForeignKey(
        Listings, on_delete=models.CASCADE, related_name='comments', verbose_name='Объявление')
    author = models.CharField(max_length=30, verbose_name='Автор')
    content = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(
        default=True, db_index=True, verbose_name='Выводить на экран?')
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Опубликован')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['-created_at']
