from django.contrib import admin
from .models import Listings
from django.apps import AppConfig






class ListingAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'title', 'is_published','price', 'city', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', )
    list_editable = ('is_published', )
    list_per_page = 25
    search_fields = ('title',)
    name = 'frontend'
    verbose_name = "Your Home Page"



# Register your models here.
admin.site.register(Listings, ListingAdmin)
