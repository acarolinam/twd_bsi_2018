from django.contrib import admin
from .models import Category, Page, UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    # list_display = ('category', 'title', 'url')
    list_display = ('category', 'title', 'views')
    list_filter = ('category',)
    ordering = ('views', 'category', 'title')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)