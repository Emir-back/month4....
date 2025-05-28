from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse

from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm

class RecipeListView(ListView):
    model = Recipe
    template_name = 'foods/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'foods/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'foods/recipe_form.html'
    success_url = reverse_lazy('recipe-list')


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'foods/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe-list')


def add_ingredient_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('recipe-detail', pk=pk)
    else:
        form = IngredientForm()
    return render(request, 'foods/add_ingredient.html', {'form': form, 'recipe': recipe})
