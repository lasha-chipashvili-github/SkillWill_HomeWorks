from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework.views import APIView
from .models import CustomUser
from .forms import CustomUserForm
from django.urls import reverse_lazy


class CustomUserListView(APIView,ListView):
    model = CustomUser
    context_object_name = 'user_list'
    queryset = CustomUser.objects.all()
    template_name = 'user/list_users.html'

def create_custom_user(request):
    if request.method == 'POST':

        form = CustomUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('user_list'))
    else:
        form = CustomUserForm()
    return render(request, 'user/user_create.html', {'form':form,'current_page':"CREATE"})


def change_custom_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'user/change_custom_user.html', {'form': form, 'current_page':"EDIT"})

def delete_custom_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user/custom_user_delete.html', {'user': user,  'current_page':"DELETE"})


def custom_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    return render(request, 'user/custom_user.html', {'user': user, 'current_page':"DETAILS"})




#%% hypothetic code

# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from .serializers import CustomUserSerializer
# from rest_framework.response import Response
# from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
# from rest_framework.decorators import api_view, renderer_classes
# class CustomUserListView(ListView):
#         # renderer_classes = (TemplateHTMLRenderer,)
#
#     @api_view(('GET',))
#     @renderer_classes((TemplateHTMLRenderer,JSONRenderer))
#     def get(self, request, pk=None):
#         if pk:
#             data = CustomUser.objects.get(pk=pk)
#             serializer = CustomUserSerializer(data, context={'request': request}, many=False)
#             return Response(serializer.data)
#         data = CustomUser.objects.all()
#         serializer = CustomUserSerializer(data, context={'request': request}, many=True)
#         return Response(serializer.data, template_name='user/list_users.html')

# class CustomUserCreateView(CreateView):
#     model = CustomUser
#     fields = ('email', 'password', 'date_of_birth')