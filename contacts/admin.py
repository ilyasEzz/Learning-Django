from django.contrib import admin
from .models import Contact, Comment


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email',
                    'phone', 'contact_date', )
    list_display_links = ('id', 'name')
    list_per_page = 25
    search_fields = ('id', 'name', 'listing', 'email')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'listings', 'created_at', 'is_active')
    list_display_links = ('id', 'author')
    list_per_page = 25
    list_filter = ('author', 'listings', 'is_active', )


# register the changes
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)
