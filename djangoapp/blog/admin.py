from blog.models import Category, Page, Post, Tag
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


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
    
@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 'is_published',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'content',
    prepopulated_fields = {
        "slug": ("title", )
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
class PostAdmin(SummernoteModelAdmin):
    '''Admin View for Post'''

    list_display = ('id', "title", "is_published", "created_at")
    list_display_links = ("title",)
    readonly_fields = ('created_at', "updated_at", "updated_by", "created_by", 
                       )
    search_fields = ('id', "title", "slug", "created_at")
    list_per_page = 50
    list_filter = ("category", "is_published")
    list_editable = ("is_published", )
    ordering = ("-id",)
    prepopulated_fields = {
        "slug": ("title", )
    }
    autocomplete_fields = ("tag", "category")
    summernote_fields = ("content",)

    def save_model(self, request, obj, form, change) -> None:
        if change:
            obj.updated_by = request.user
            obj.save()
            return
        obj.created_by = request.user
        obj.save()
