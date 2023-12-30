from blog.models import Tag
from django.contrib import admin


# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'slug')
    list_display_links = ("name",)
    list_filter = ('id',)
    search_fields = ("id", 'name', 'slug')
    list_per_page = 10
    ordering = ('id',)
    prepopulated_fields = {
        "slug": ("name", )
    }