from django.urls import path
from .views import PostDetail, PostList, PostCreateView

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('add/', PostCreateView.as_view(), name='post-addition'),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
]