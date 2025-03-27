from django.urls import path
from . import views

urlpatterns = [
    path('all_hashtags_books/', views.all_category_books, name='all'),
    path('teens_category_books/', views.teens_category_books, name='teens'),
    path('kids_category_books/', views.kids_category_books, name='kids'),
]