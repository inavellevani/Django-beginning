# Generated by Django 5.0.4 on 2024-04-10 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_alter_book_options_alter_book_author_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-price'], 'verbose_name': 'Book'},
        ),
    ]
