from django.contrib import admin
from rango.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'views')
    list_filter = ('category',)
    ordering = ('views', 'category', 'title')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)