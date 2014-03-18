from django.shortcuts import render
from rest_framework import viewsets, renderers, generics
from app.models import User, Cliente
from app.serializers import UserSerializer, ClienteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = ()
    # renderer_classes = [renderers.JSONRenderer, ]


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

def index(request):
    return render(request, 'app/index.html', {})