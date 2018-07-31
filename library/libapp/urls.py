from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    url(r'login/', auth_views.login, name='login'),
    url(r'logout/', auth_views.logout, {'next_page': '/book/login/'}, name='logout'),
    url(r'register/', views.registration, name='register'),
    url(r'book_data/', views.get_books_data, name='book_data'),
    url(r'all_books/', views.BookView.as_view()),
    url(r'book_form/', views.book_view, name='book_form'),
    #url(r'create_book/', views.create_book),
    url(r'home/', views.home, name='home')
]
