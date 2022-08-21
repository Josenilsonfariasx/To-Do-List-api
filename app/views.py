from .serializers import TodoSerializer
from .models import Todo
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class TodoListAndCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer