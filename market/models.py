from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from market.choices import choices as cover_choices
from django.utils.translation import gettext_lazy as _
from modeltranslation.translator import register, TranslationOptions
import os


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Author's Name"))

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Category Name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Categories")


class Book(models.Model):
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name=_("Author"))
    category = models.ManyToManyField(Category, verbose_name=_("Categories"))
    name = models.CharField(max_length=100, verbose_name=_("Book Title"))
    page_count = models.IntegerField(verbose_name=_("Number of Pages"))
    price = models.IntegerField(verbose_name=_("Price"))
    cover_type = models.CharField(
        max_length=2,
        choices=cover_choices,
        default='HC',
        verbose_name=_("Cover type")
    )
    image = models.ImageField(upload_to='', blank=True, null=True, verbose_name=_("Book Cover"))

    class Meta:
        verbose_name =_("Book")
        ordering = ["-price"]

    def __str__(self):
        return self.name


def register_translations():
    @register(Author)
    class AuthorTranslationOptions(TranslationOptions):
        fields = ('name',)

    @register(Category)
    class CategoryTranslationOptions(TranslationOptions):
        fields = ('name',)

    @register(Book)
    class BookTranslationOptions(TranslationOptions):
        fields = ('name', 'cover_type')


@receiver(pre_delete, sender=Book)
def delete_book_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
