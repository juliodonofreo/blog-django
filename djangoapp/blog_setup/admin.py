from blog_setup.models import MenuLink, SiteSetup
from django.contrib import admin


# Register your models here.
class MenuLinkInline(admin.TabularInline):
    '''Tabular Inline View for MenuLink'''
    model = MenuLink
    extra = 1
    
    
@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    inlines = (MenuLinkInline),
    
    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()
