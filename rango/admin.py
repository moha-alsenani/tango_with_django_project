from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')  # Fields to display in the list view
    list_filter = ('category',)  # adding a filter option by category
    search_fields = ('title', 'url')  # allowing searching by title and URL

admin.site.register(Category)
admin.site.register(Page, PageAdmin) # Register the Category and Page models with the customized admin interface

