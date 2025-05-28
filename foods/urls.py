from django.urls import path
from .views import (
    RecipeListView, RecipeDetailView, RecipeCreateView,
    RecipeDeleteView, add_ingredient_view
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('recipe/<int:pk>/ingredient/add/', add_ingredient_view, name='ingredient-add'),
]
