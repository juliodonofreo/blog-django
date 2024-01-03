from django.contrib.auth import get_user_model
from django.db import models
from django_summernote.models import AbstractAttachment
from utils import image
from utils.rands import random_slugify

# Create your models here.


class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
        current_file_name = str(self.file.name)
        super().save(*args, **kwargs)
        file_changed = False

        if self.file:
            file_changed = current_file_name != self.file.name

        if file_changed:
            image.resize_image(self.file, 900, True, 70)
    
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


class Post(models.Model):
    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=False,
        blank=True,
        max_length=255
    )
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(("Publicado"),
                                       default=False,
                                       help_text="Este campo torna o post \
                                       pública")
    content = models.TextField()
    cover = models.ImageField(upload_to="posts/", blank=True, default="")
    cover_in_post_content = models.BooleanField(default=True,
                                                help_text="Exibe a capa dentro\
                                                do post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                                   blank=True, null=True,
                                   related_name="post_created_by")
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                                   null=True,
                                   related_name="post_updated_by")
    category = models.ForeignKey(Category, verbose_name=("categories"),
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 default=None)
    tag = models.ManyToManyField(Tag, blank=True, default='', related_name="tag_set")

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random_slugify(self.title, 5)
        current_cover_name = str(self.cover.name)
        super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            image.resize_image(self.cover, 900, True, 70)
