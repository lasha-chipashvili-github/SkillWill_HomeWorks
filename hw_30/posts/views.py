from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets, generics
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Post
from .serializers import PostSerializer

# Create your views here.

#
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # template_name = "posts/post_list.html"
    #
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     context = {'data': serializer.data}
    #     return render(request, self.template_name, context)



from django.views import View
from .forms import PostForm

class PostUpdateView(View):
    template_name = 'posts/post_update.html'

    def get(self, request, pk, *args, **kwargs):
        obj = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=obj)
        return render(request, self.template_name, {'form': form, 'obj': obj})

    def post(self, request, pk, *args, **kwargs):
        obj = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form, 'obj': obj})

def delete_post(request, pk):
    obj = get_object_or_404(Post, pk=pk)
    obj.delete()
    return redirect('post_list')
