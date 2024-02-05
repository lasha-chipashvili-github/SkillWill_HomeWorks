from django.contrib.auth.models import User
# from .models import UserRecipe
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


# class UserRecipeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserRecipe
#         fields = ('id', 'user', 'recipe')