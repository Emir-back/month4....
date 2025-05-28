from django.urls import path
from .views import ParserForm, FilmixListView


urlpatterns = [
    path('parser_form/',ParserForm.as_view(), name='parser_form'),
    path('parser_list/', FilmixListView.as_view(), name='parser_list'),

] 