from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

GENDER = (("Male", "Male"), ("Female", "Female"))

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    phone_number = forms.CharField(required=True, label='Номер телефона')
    age = forms.IntegerField(required=True, label='Возраст')
    gender = forms.ChoiceField(choices=GENDER, required=True, label='Пол')
    experience = forms.IntegerField(required=True, label="Опыт работы (кол-во)")
    diploma = forms.CharField(required=True, label="Диплом")
    address = forms.CharField(required=True, label="Адрес")
    city = forms.CharField(required=True, label="Город")
    country = forms.CharField(required=True, label="Страна")

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number',
            'experience',
            'diploma',
            'address',
            'city',
            'country',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.age = self.cleaned_data['age']
        user.gender = self.cleaned_data['gender']
        user.experience = self.cleaned_data['experience']
        user.diploma = self.cleaned_data['diploma']
        user.address = self.cleaned_data['address']
        user.city = self.cleaned_data['city']
        user.country = self.cleaned_data['country']

        if commit:
            user.save()
        return user

