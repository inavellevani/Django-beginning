from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from market.models import Book, Author, Category
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import activate


def book_list(request):
    books = Book.objects.all()

    author_name = request.GET.get('author')
    if author_name:
        authors = Author.objects.filter(name__icontains=author_name)
        books = books.filter(author_name__in=authors)

    category_name = request.GET.get('category')
    if category_name:
        categories = Category.objects.filter(name__icontains=category_name)
        books = books.filter(category__in=categories)

    paginator = Paginator(books, 3)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    if request.headers.get('Accept') == 'application/json':
        data = serializers.serialize('json', page_obj)
        return JsonResponse(data, safe=False)
    else:
        context = {'page_obj': page_obj}
        return render(request, 'welcome.html', context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.headers.get('Accept') == 'application/json':
        data = serializers.serialize('json', [book])
        return JsonResponse(data, safe=False)
    else:
        context = {'book': book}
        return render(request, 'book_detail.html', context)


def welcome(request):
    return book_list(request)


def set_language(request):
    language = request.GET.get('language', None)
    if language:
        activate(language)
    return redirect(request.META.get('HTTP_REFERER', '/'))
