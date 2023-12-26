from blog_setup.models import MenuLink
from django.contrib import admin


# Register your models here.
@admin.register(MenuLink)
class Admin(admin.ModelAdmin):

    list_display = ("id", 'text', 'url_or_path')
    list_display_links = ("id", "text", "url_or_path")
    list_filter = ('id',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('id', 'text', 'url_or_path')
    # date_hierarchy = ''
    ordering = ('id',)