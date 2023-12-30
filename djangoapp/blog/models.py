from django.db import models
from utils.rands import random_slugify


# Create your models here.
class Tag(models.Model):
    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")
        
    name = models.CharField(("Name"), max_length=255)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True, 
        blank=True,
        max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random_slugify(self.name, 5)
        return super().save(*args, **kwargs)

