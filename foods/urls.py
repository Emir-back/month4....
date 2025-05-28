from django.urls import path
from .views import (
    RecipeListView, RecipeDetailView,
    RecipeCreateView, RecipeDeleteView,
    IngredientCreateView
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('ingredient/add/', IngredientCreateView.as_view(), name='ingredient-add'),
]
