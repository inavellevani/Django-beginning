# Generated by Django 5.0.4 on 2024-04-15 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
