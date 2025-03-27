from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path('books_list/<int:id>/', views.books_detail, name='books_detail'),
    path('search/', views.SearchBookView.as_view(), name='search_books'),
]