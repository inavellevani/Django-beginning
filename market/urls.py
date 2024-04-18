from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from market.views import book_list, book_detail, set_language
from market.views import welcome
from market import views


urlpatterns = [
    path('api/books/', book_list, name='book_list'),
    path('api/books/<int:book_id>/', book_detail, name='book_detail'),
    path('', welcome, name='welcome'),
    path('language/', set_language, name='set_language'),
]
