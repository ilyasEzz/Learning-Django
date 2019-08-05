from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'phone', 'contact_date', )
    list_display_links = ('id', 'name')
    list_per_page = 25
    search_fields = ('id', 'name', 'listing', 'email') 


# register the changes
admin.site.register(Contact, ContactAdmin)