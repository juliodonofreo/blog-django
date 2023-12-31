from django.db import models
from utils import image, model_validators


# Create your models here.
class SiteSetup(models.Model):
    class Meta:
        verbose_name = "Setup"
        verbose_name_plural = "Setup"

    title = models.CharField(("title"), max_length=65)
    description = models.CharField(("description"), max_length=255)

    show_header = models.BooleanField(("show header?"), default=True)
    show_search = models.BooleanField(("show search?"), default=True)
    show_menu = models.BooleanField(("show menu?"), default=True)
    show_description = models.BooleanField(("show description?"), default=True)
    show_pagination = models.BooleanField(("show pagination?"), default=True)
    show_footer = models.BooleanField(("show footer?"), default=True)
    
    favicon = models.ImageField(("Icon"),
                                upload_to="assets/favicon", 
                                blank=True, 
                                default="",
                                validators=[model_validators.validate_png], 
                                help_text="A imagem deve ser .png")

    def save(self, *args, **kwargs):
        current_favicon_name = str(self.favicon.name)
        super().save(*args, **kwargs)
        favicon_changed = False

        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name

        if favicon_changed:
            image.resize_image(self.favicon, 32)

    def __str__(self):
        return str(self.title)


class MenuLink (models.Model):
    class Meta:
        verbose_name = "Menu link"
        verbose_name_plural = "Menu links"

    text = models.CharField(("Text"), max_length=50)
    url_or_path = models.CharField(("Url or path"), max_length=2048)
    new_tab = models.BooleanField(("New tab?"), default=False, name="new_tab")

    site_setup = models.ForeignKey(SiteSetup, on_delete=models.CASCADE,
                                   blank=True, null=True)

    def __str__(self):
        return str(self.text)
