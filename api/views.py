from rest_framework import viewsets
from rest_framework import generics
from .serializers import TodoSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from .models import Todo


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
