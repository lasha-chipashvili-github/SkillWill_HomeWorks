from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.views import APIView


# Create your views here.

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):
        if request.user.is_authenticated:
            return Response({'message': 'You are already logged'})

        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(data={'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        return Response(status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, redirect='login'):
        logout(request)
        return Response(status=status.HTTP_200_OK)


# Create your views here.
