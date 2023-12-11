from django.urls import path
from .views import animal

urlpatterns = [
    path("animal/", animal, name="animal")
]