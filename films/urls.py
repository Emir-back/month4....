from django.urls import path
from . import views

urlpatterns = [
    path('film_list/', views.FilmListView.as_view(), name='film_list'),  # главная страница со списком фильмов
    path('film_list/<int:id>/', views.FilmDetailView.as_view(), name='film_detail'),
    path('film_list/<int:id>/delete/', views.DeleteFilmView.as_view(), name='delete_film'), 
    path('film_list/<int:id>/update/', views.UpdateFilmView.as_view(), name='update_film'),
    path('create_film/', views.CreateFilmView.as_view(), name='create_film'),
    path('search/',views.SearchFilmView.as_view(),name='search'),
]