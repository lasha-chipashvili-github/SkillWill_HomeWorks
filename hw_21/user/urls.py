from django.urls import path, include

from .views import CustomUserListView , create_custom_user, change_custom_user, delete_custom_user, custom_user

urlpatterns = [
    path((''), CustomUserListView.as_view(), name='/'),
    path(('users/'), CustomUserListView.as_view(), name='user_list'),
    path('users/create', create_custom_user, name='user_create'),
    path('users/<int:pk>', custom_user, name='user_detail'),
    path('users/<int:pk>/change', change_custom_user, name='user_change'),
    path('users/<int:pk>/delete', delete_custom_user, name='user_delete'),

]