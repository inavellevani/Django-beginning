from django.contrib import admin
from market.models import Book


class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'category', 'price')
    search_fields = ('name', 'author_name')


admin.site.register(Book, BooksAdmin)
