from django import forms
from . import models, parser_rezka, parser_neb_kg


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('Rezka.ag', 'Rezka.ag'),
        ('Neb.kg', 'Neb.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'Rezka.ag':
            rezka_films = parser_rezka.parsing_rezka()
            for i in rezka_films:
                i.pop('image', None)
                models.RezkaFilmsModel.objects.create(**i)

        elif self.data['media_type'] == 'Neb.kg':
            neb_books = parser_neb_kg.parsing_neb_kg()
            for i in neb_books:
                i.pop('image', None)
                models.NebKgBooksModel.objects.create(**i)