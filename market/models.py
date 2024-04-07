from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os


class Book(models.Model):
    name = models.CharField(max_length=100)
    page_count = models.IntegerField()
    category = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.name


@receiver(pre_delete, sender=Book)
def delete_book_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
