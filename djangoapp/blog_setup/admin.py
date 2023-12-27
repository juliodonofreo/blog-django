from blog_setup.models import MenuLink, SiteSetup
from django.contrib import admin


# Register your models here.
@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):

    list_display = ("id", 'text', 'url_or_path')
    list_display_links = ("id", "text", "url_or_path")
    list_filter = ('id',)
    search_fields = ('id', 'text', 'url_or_path')
    ordering = ('id',)
    
@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    
    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()
