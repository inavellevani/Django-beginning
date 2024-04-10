from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name="Book Title")
    page_count = models.IntegerField(verbose_name="Number of Pages")
    category = models.CharField(max_length=100, verbose_name="Category")
    author_name = models.CharField(max_length=100, verbose_name="Author")
    price = models.IntegerField(verbose_name="Price")
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
