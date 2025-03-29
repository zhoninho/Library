from django.contrib import admin
from . import models
from django.core.exceptions import ValidationError
from django import forms
from PIL import Image
from .models import Books, Reviews


# Форма для проверки размеров изображения
class ImageForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

    def clean_image(self):
        image = self.cleaned_data.get("image")
        print("Метод clean_image вызван!")  # Проверка
        if not image:
            return image

        try:
            with Image.open(image) as img:
                width, height = img.size
                print(f"Ширина: {width}, Высота: {height}")

                if width > 700 or height > 500:
                    raise ValidationError(
                        "Размер картинки слишком большой. Загрузите изображение 1200x1000 или меньше.")
        except Exception as e:
            raise ValidationError(f"Ошибка обработки изображения: {e}")

        return image


# Админка для фильмов
class BooksAdmin(admin.ModelAdmin):
    form = ImageForm
    list_display = ("title", "image")  # Добавляем нужные поля


# Регистрируем модели
admin.site.register(Books, BooksAdmin)
admin.site.register(Reviews)

# admin.site.register(models.Books)
# admin.site.register(models.Reviews)
