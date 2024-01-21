from rest_framework import generics, permissions, status

from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer, PostPUTSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostPUTSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        title = serializer.validated_data['title']
        post_body = serializer.validated_data['post_body']
        post_cat = serializer.validated_data['post_cat']

        user = self.request.user
        post = Post(title=title, post_body=post_body, author=user, post_cat=post_cat)
        post.save()

        return Response(status=status.HTTP_201_CREATED)

