from rest_framework import viewsets
from .models import Recipe

from rest_framework import generics
from rest_framework import permissions


from .serializers import RecipeSerializer



# class RecipeView(viewsets.ModelViewSet):
#      serializer_class = UserRecipeSerializer
#      queryset = UserRecipe.objects.all()
#      def get_queryset(self):
#           user = self.request.user
#           queryset = UserRecipe.objects.filter(user=user)


# class RecipeView(viewsets.ModelViewSet):
#      queryset= Recipe.objects.all()
#      serializer_class= RecipeSerializer



class RecipeView(viewsets.ModelViewSet):
    # queryset= Recipe.objects.all()
    def get_queryset(self):
        user = self.request.user
        queryset = Recipe.objects.filter(user=user)
        return queryset

    serializer_class= RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

# class RecipeCreateView(generics.CreateAPIView):
#     serializer_class = RecipeSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
