from rest_framework import serializers
from .models import Recipe
from django.contrib.auth.models import User

class RecipeSerializer(serializers.ModelSerializer):
   class Meta:
       model = Recipe
       fields = ('id','name','ingredient','time','process',
                 'user'
                 )

       def create(self, validated_data):
           user = self.context['request'].user
           validated_data['user'] = user
           return super().create(validated_data)