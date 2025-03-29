from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache

class SearchBookView(generic.ListView):
    template_name = 'books_list.html'
    context_object_name = 'query'

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

#get id
class BooksDetailView(generic.DetailView):
    model = models.Books
    template_name = 'book_detail.html'
    context_object_name = 'books_id'

    def get_object(self):
        return get_object_or_404(models.Books, id=self.kwargs['id'])

#list
@method_decorator(cache_page(60*15), name='dispatch')
class BooksListView(generic.ListView):
     model = models.Books
     template_name = 'books_list.html'
     context_object_name = 'query'

     def get_queryset(self):
         books = cache.get('query')
         if not books:
             books = self.model.objects.all()
             cache.set('query', books)
         return books

