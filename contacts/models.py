from django.db import models
from datetime import datetime

from listings.models import Listings

# Create your models here.


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Контакты"


class Comment(models.Model):
    listings = models.ForeignKey(
        Listings, on_delete=models.CASCADE, verbose_name='Объявление')
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
