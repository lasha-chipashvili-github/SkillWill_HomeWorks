from django.urls import path
from .views import SelectCarView, AddCarView, DeleteCarView

urlpatterns = [
    path("", SelectCarView.as_view(), name="SelectAllCars"),
    path("<int:pk>", SelectCarView.as_view(), name="SelectConcreteCar"),
    path("add", AddCarView.as_view(), name="AddCar"),
    path("delete/<int:pk>", DeleteCarView.as_view(), name="DeleteCar"),
]