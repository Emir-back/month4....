from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from . import models,forms 


class FilmixListView(generic.ListView):
    template_name = 'parser_library/parser_book_list.html'
    model = models.Parser_filmix # Replace with the actual model name
    context_object_name = 'filmix'

    def get_queryset(self):
        return self.model.objects.all()
    
class ParserForm(generic.FormView):
    template_name = 'parser_library/parser_form.html'
    form_class = forms.ParserFilmix # Replace with the actual form class name
    

    def post(self, request, *args, **kwargs):
        form= self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1> парсин успешно завершен<h1>')
        else:
            return super(ParserForm, self).post(request, *args, **kwargs)
        