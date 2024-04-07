from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from market.models import Book


def book_list(request):
    books = Book.objects.all()
    data = [
        {
            'name': book.name,
            'page_count': book.page_count,
            'category': book.category,
            'author_name': book.author_name,
            'price': float(book.price),
            'image': request.build_absolute_uri(book.image.url) if book.image else None

        }
        for book in books
    ]
    return JsonResponse({'books': data})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    data = {
        'name': book.name,
        'page_count': book.page_count,
        'category': book.category,
        'author_name': book.author_name,
        'price': float(book.price),
        'image': request.build_absolute_uri(book.image.url) if book.image else None
    }
    return JsonResponse(data)


def welcome(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'welcome.html', context)
