from django.db import models
from books.models import Books


class ProductList(models.Model):
    STATUS = (
        ('✅', '✅'),
        ('❌', '❌')
    )
    title = models.CharField(max_length=100)
    choice_books = models.ForeignKey(Books, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='❌')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
