from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from posts import serializers
from .models import Post
from .serializers import PostSerializer
from .utils import Redis


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_queryset(self):
    #
    #     cached_data = Redis.get('PostAPICall')
    #
    #     if cached_data:
    #         queryset = cached_data
    #         return queryset
    #
    #     data = Post.objects.all()
    #     serializer = serializers.PostSerializer(data, many=True)
    #     Redis.set('PostAPICall', serializer.data)
    #     queryset = serializer.data
    #     return queryset

    def list(self, request, *args, **kwargs):
        cached_data = Redis.get('PostAPICall')

        if cached_data:
            queryset = cached_data
            return queryset

        data = Post.objects.all()
        serializer = serializers.PostSerializer(data, many=True)
        Redis.set('PostAPICall', serializer.data)

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return super().get_permissions()