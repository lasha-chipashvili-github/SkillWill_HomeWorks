from django.urls import path

from .views import FilmListView, FilmDetailView, FilmCreateView

urlpatterns = [
    path('films/', FilmListView.as_view(), name='film_list'),
    path('films/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('films/add/', FilmCreateView.as_view(), name='film_create'),
]