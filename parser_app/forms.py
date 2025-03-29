from django import forms
from . import models, parser_rezka


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('Rezka.ag', 'Rezka.ag'),
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