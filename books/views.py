from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models


#get id
def books_detail(request, id):
    if request.method == 'GET':
        books_id = get_object_or_404(models.Books, id=id)
        return render(
            request,
            template_name='book_detail.html',
            context={
                'books_id': books_id,
            }
        )


#list
def books_list(request):
    if request.method == 'GET':
        query = models.Books.objects.all()
        return render(
            request,
            template_name='books_list.html',
            context={
                'query': query,
            }
        )

