from django.shortcuts import render , get_object_or_404
from . import models,forms
from django.http import HttpResponse

def update_film_view(request,id):
    film_id = get_object_or_404(models.Film, id=id)
    if request.method == "POST":
        form = forms.FilmForm(request.POST,instance=film_id)
        if form.is_valid():
            form.save()
            return HttpResponse('Книга успешно обновлена')
        else:
            form = forms.FilmForm(instance=film_id)
            return render(request,template_name='books/update_film.html' , context = {
                'form' : form,
                'film_id' : film_id,
            })


def delete_film_view(request , id):
    film_id = get_object_or_404(models.Film, id=id)
    film_id.delete()
    return HttpResponse('Книга успешно удалена')






def create_film_view(request):
    if request.method == 'POST':
        form = forms.FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return HttpResponse('Фильм успешно добавлен')
    else:
        form = forms.FilmForm()  

    return render(request, 'books/create_film.html', {'form': form})




def film_list_view(request):
    if request.method == 'GET':
        film = models.Film.objects.all().order_by('-id')
        context = {
            'film': film
        }
        return render(request, 'books/book_list.html', context=context)

def film_detail_view(request,id):
    if request.method == 'GET':
        film_id = get_object_or_404(models.Film, id=id)
        context = {
            'film_id':film_id,
        }
        return render(request,
                      template_name='books/book_detail.html',
                      context=context,
                      )