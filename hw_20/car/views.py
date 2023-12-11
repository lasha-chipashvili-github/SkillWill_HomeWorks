from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car
from .serializers import CarSerializer

# Create your views here.
# def car(request):
#     return render('car.html')

class SelectCarView(APIView):

    def get(self, request, pk=None):
        if pk:
            data = Car.objects.get(pk=pk)
            serializer = CarSerializer(data, context={'request': request}, many=False)
            return Response(serializer.data)
        data = Car.objects.all()
        serializer = CarSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

class AddCarView(APIView):

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteCarView(APIView):

    def delete(self, request, pk):
        event = Car.objects.get(pk=pk)
        event.delete()
        return Response("Car deleted successfully!")

