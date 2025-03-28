from django.contrib.auth.models import User
from django.db import models

class CustomUser(User):
    DEGREE_CHOICES_DICT = {
        "bachelor": ("Библиотекарь", 40000),
        "master": ("Главный библиотекарь", 50000),
        "docent": ("Директор", 55000),
        "college": ("Помощник библиотекаря", 10000),
    }

    DEGREE_CHOICES = [(key, value[0]) for key, value in DEGREE_CHOICES_DICT.items()]

    phone_number = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")], default="Robot")
    experience = models.IntegerField(default=0)
    diploma = models.CharField(max_length=255, blank=True, null=True, default="none", choices=DEGREE_CHOICES)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    salary = models.IntegerField(default=0)
    position = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        degree_data = self.DEGREE_CHOICES_DICT.get(self.diploma)
        if degree_data:
            self.position, self.salary = degree_data
        else:
            self.position = "none"
            self.salary = 0

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
