from django.urls import path
from .views import (
    # PostViewSet
    PostListView,
    PostUpdateView,
    delete_post,
)
from rest_framework.routers import DefaultRouter

#
# router = DefaultRouter()
# router.register(r'posts', PostViewSet, basename="post")
#
# urlpatterns = router.urls

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>/", delete_post, name='post_delete'),
]