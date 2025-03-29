from django.urls import path
from . import views

urlpatterns = [
    path('', views.BooksListView.as_view(), name='books_list'),
    path('books_list/<int:id>/', views.BooksDetailView.as_view(), name='books_detail'),
    path('search/', views.SearchBookView.as_view(), name='search_books'),
]