from django.shortcuts import render , get_object_or_404
from . import models,forms
from django.http import HttpResponse
from django.views import generic


class SearchFilmView(generic.ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'film'
    paginate_by = 5
    model = models.Film

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('q'))
    def get_context_data(self,*,object_list = None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

class UpdateFilmView(generic.UpdateView):
    template_name = 'books/update_film.html'

    form_class = forms.FilmForm
    success_url = '/films/film_list/'
      
    def get_object(self,  **kwargs):      
        film_id = self.kwargs.get('id')      
        return get_object_or_404(models.Film, id=film_id)      
    def form_valid(self, form):      
        print(form.cleaned_data)      
        return super(UpdateFilmView, self).form_valid(form=form)  





      
      
# def update_film_view(request, id):
#     film = get_object_or_404(models.Film, id=id)

#     if request.method == "POST":
#         form = forms.FilmForm(request.POST, instance=film)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Фильм успешно обновлен')
#         else:
            
#             return render(request, 'books/update_film.html', {
#                 'form': form,
#                 'film_id': film.id
#             })
#     else:
        
#         form = forms.FilmForm(instance=film)
#         return render(request, 'books/update_film.html', {
#             'form': form,
#             'film_id': film.id
#         })

class DeleteFilmView(generic.DeleteView):
    template_name = 'books/confirm_delete.html'
    success_url = '/films/film_list/'
    def get_object(self,**kwargs):
         film_id = self.kwargs.get('id')
         return get_object_or_404(models.Film, id=film_id)
# def delete_film_view(request , id):
#     film_id = get_object_or_404(models.Film, id=id)
#     film_id.delete()
#     return HttpResponse('Книга успешно удалена')




class CreateFilmView(generic.CreateView):
    template_name = 'books/create_film.html'
    form_class = forms.FilmForm
    success_url = '/films/film_list/'
 
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateFilmView, self).form_valid(form=form)




# def create_film_view(request):
#     if request.method == 'POST':
#         form = forms.FilmForm(request.POST, request.FILES)
#         if form.is_valid(): 
#             form.save()  
#             return HttpResponse('Фильм успешно добавлен')
#     else:
#         form = forms.FilmForm()  

#     return render(request, 'books/create_film.html', {'form': form})



class FilmListView(generic.ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'film'
    model = models.Film

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
# def film_list_view(request):
#     if request.method == 'GET':
#         film = models.Film.objects.all().order_by('-id')
#         context = {
#             'film': film
#         }
#         return render(request, 'books/book_list.html', context=context)

class FilmDetailView(generic.DetailView):
    template_name = 'books/book_detail.html'

    def get_object(self,**kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.Film , id=film_id)





# def film_detail_view(request,id):
#     if request.method == 'GET':
#         film_id = get_object_or_404(models.Film, id=id)
#         context = {
#             'film_id':film_id,
#         }
#         return render(request,
#                       template_name='books/book_detail.html',
#                       context=context,
#                       )