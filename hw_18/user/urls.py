from django.urls import path
from .views import show_user

urlpatterns = [
    path("", show_user, name="user")
]