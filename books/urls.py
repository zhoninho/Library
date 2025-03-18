from django.urls import path
from . import views

urlpatterns = [
    path('books_list/', views.books_list, name='books_list'),
    path('books_list/<int:id>/', views.books_detail, name='books_detail'),
]