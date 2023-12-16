from rest_framework import serializers
from .models import CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'date_of_birth']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password')

        if validated_data['password'] != confirm_password:
            raise serializers.ValidationError('Passwords do not match')

        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user