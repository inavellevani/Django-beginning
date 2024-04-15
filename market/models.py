from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from market.genres import genre_choices
import os


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Author's Name")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        choices=genre_choices,
        verbose_name="Category Name",

    )

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name="Book Title")
    page_count = models.IntegerField(verbose_name="Number of Pages")
    category = models.ManyToManyField(Category, verbose_name="Categories")
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name="Author")
    price = models.IntegerField(verbose_name="Price")
    cover_type = models.CharField(
        max_length=2,
        choices=[('HC', 'Hardcover'), ('PB', 'Paperback'), ('SP', 'Special')],
        default='HC',
        verbose_name="Cover type"
    )
    image = models.ImageField(upload_to='', blank=True, null=True, verbose_name="Book Cover")

    class Meta:
        verbose_name = "Book"
        ordering = ["-price"]

    def __str__(self):
        return self.name


@receiver(pre_delete, sender=Book)
def delete_book_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

