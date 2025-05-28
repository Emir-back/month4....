from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
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

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'foods/ingredient_form.html'
    success_url = reverse_lazy('recipe-list')

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'foods/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe-list')
