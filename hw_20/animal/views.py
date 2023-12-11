from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Animal
from .serializers import AnimalSerializer


class SelectAnimalView(APIView):

    def get(self, request, pk=None):
        if pk:
            data = Animal.objects.get(pk=pk)
            serializer = AnimalSerializer(data, context={'request': request}, many=False)
            return Response(serializer.data)
        data = Animal.objects.all()
        serializer = AnimalSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

class AddAnimalView(APIView):

    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteAnimalView(APIView):

    def delete(self, request, pk):
        event = Animal.objects.get(pk=pk)
        event.delete()
        return Response("Animal deleted successfully!")
