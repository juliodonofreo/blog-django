from blog.models import Category, Page, Post, Tag
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
    
@admin.register(Post)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('id', "title", "is_published", "created_at")
    list_display_links = ("title",)
    readonly_fields = ('created_at', "updated_at", "updated_by", "created_by",)
    search_fields = ('id', "title", "slug", "created_at")
    list_per_page = 50
    list_filter = ("category", "is_published")
    list_editable = ("is_published", )
    ordering = ("-id",)
    prepopulated_fields = {
        "slug": ("title", )
    }
    autocomplete_fields = ("tag", "category")