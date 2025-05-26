from django import forms
from . import models, parser_filmix

class ParserFilmix(forms.Form):
    MEDIA_CHOICES = [
        ('filmix.ag', 'filmix.ag'),
    ]

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    def parser_data(self):
        if self.cleaned_data['media_type'] == 'filmix.ag':  
            filmix_film = parser_filmix.parsing_filmix() or []  
            for i in filmix_film:
                try:
                    models.Parser_filmix.objects.create(**i)
                except Exception as e:
                    print(f"Ошибка при сохранении объекта: {e}")
