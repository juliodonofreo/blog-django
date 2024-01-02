from blog.models import Category, Page, Tag
from django.contrib import admin


# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'slug')
    list_display_links = ("name",)
    list_filter = ('id',)
    search_fields = ('name', 'slug')
    list_per_page = 10
    ordering = ('id',)
    prepopulated_fields = {
        "slug": ("name", )
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'slug')
    list_display_links = ("name",)
    list_filter = ('id',)
    search_fields = ('name', 'slug')
    list_per_page = 10
    ordering = ('id',)
    prepopulated_fields = {
        "slug": ("name", )
    }
    
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'slug')
    list_display_links = ("title",)
    list_filter = ('id',)
    search_fields = ('title', 'slug')
    list_per_page = 10
    ordering = ('id',)
    prepopulated_fields = {
        "slug": ("title", )
    }