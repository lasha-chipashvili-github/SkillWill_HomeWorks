from django.urls import path
from .views import AddAnimalView, SelectAnimalView, DeleteAnimalView

urlpatterns = [
    path("", SelectAnimalView.as_view(), name="SelectAllAnimals"),
    path("<int:pk>", SelectAnimalView.as_view(), name="SelectConcreteAnimal"),
    path("add", AddAnimalView.as_view(), name="AddAnimal"),
    path("delete/<int:pk>", DeleteAnimalView.as_view(), name="DeleteAnimal"),
]