from django.urls import path
from market.views import book_list, book_detail
from market.views import welcome


urlpatterns = [
    path('api/books/', book_list, name='book_list'),
    path('api/books/<int:book_id>/', book_detail, name='book_detail'),
    path('', welcome, name='welcome')
]
