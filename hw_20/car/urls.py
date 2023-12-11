from django.urls import path
from .views import SelectCarView, AddCarView, DeleteCar

urlpatterns = [
    path("", SelectCarView.as_view(), name="SelectAllCars"),
    path("<int:pk>", SelectCarView.as_view(), name="SelectAllCars"),
    path("add", AddCarView.as_view(), name="AddCar"),
    path("delete/<int:pk>", DeleteCar.as_view(), name="DeleteCar"),
]