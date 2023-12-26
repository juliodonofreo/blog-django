from django.db import models


# Create your models here.
class MenuLink (models.Model):
    class Meta:
        verbose_name = "Menu link"
        verbose_name_plural = "Menu links"

    text = models.CharField(("Text"), max_length=50)
    url_or_path = models.CharField(("Url or path"), max_length=2048)
    new_tab = models.BooleanField(("New tab?"), default=False, name="new_tab")
    
    
    def __str__(self):
        return self.text
