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
    
    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random_slugify(self.name, 5)
        return super().save(*args, **kwargs)


class Category(models.Model):
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    name = models.CharField(("Name"), max_length=255)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True, 
        blank=True,
        max_length=255
    )
    
    def __str__(self): 
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random_slugify(self.name, 5)
        return super().save(*args, **kwargs)
    

class Page(models.Model):
    class Meta:
        verbose_name = ("Page")
        verbose_name_plural = ("Pages")

    title = models.CharField(("title"), max_length=50)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=False, 
        blank=True,
        max_length=255
    )
    is_published = models.BooleanField(("Publicado"), 
                                       default=False, 
                                       help_text="Este campo torna a página \
                                       pública")
    content = models.TextField()
    
    def __str__(self): 
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random_slugify(self.title, 5)
        return super().save(*args, **kwargs)
