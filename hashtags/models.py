from django.db import models

class Tags(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tags)
    def __str__(self):
        return self.title