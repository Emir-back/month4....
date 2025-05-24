from django import forms
from . import models,parser_filmix

class ParserFilmix(forms.Form):
    MEDIA_CHOICES = [
        ('filmix.ag', 'filmix.ag')
]

    


    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    def parser_data(self):
        if self.data['media_type'] == 'filmix.ag':
            filmix_film = parser_filmix.parser_filmix()
            for i in filmix_film:
                models.Parser_filmix.objects.create(**i)
            
