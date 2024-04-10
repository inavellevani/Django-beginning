from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from market.models import Book
from django.core import serializers


def book_list(request):
    books = Book.objects.all()
    data = serializers.serialize('json', books)
    return JsonResponse(data)


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    data = serializers.serialize('json', book)
    return JsonResponse(data)


def welcome(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'welcome.html', context)
