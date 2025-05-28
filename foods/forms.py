from django import forms
from .models import Ingredient , Recipe

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['title', 'description']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name','quantity']