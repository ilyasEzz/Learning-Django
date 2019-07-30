from django.contrib import admin
from .models import Listings


class ListingAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'title', 'is_published','price', 'city', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', )
    list_editable = ('is_published', )
    list_per_page = 25
    search_fields = ('title',)



# Register your models here.
admin.site.register(Listings, ListingAdmin)
