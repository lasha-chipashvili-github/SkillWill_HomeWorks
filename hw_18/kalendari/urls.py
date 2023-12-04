from django.urls import path
from .views import tarigi

urlpatterns = [
    path("", tarigi, name="kalendari")
]
