from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    # list_display = ('category', 'title', 'url')
    list_display = ('category', 'title', 'views')
    list_filter = ('category',)
    ordering = ('views', 'category', 'title')

# Register your models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)