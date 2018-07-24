from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'book_data/', views.get_books_data),
    url(r'all_books/', views.BookView.as_view()),
    url(r'book_form/', views.book_view),
    url(r'create_book/', views.create_book)
]
