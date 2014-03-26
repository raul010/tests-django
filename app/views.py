from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets, renderers, generics, mixins
from app.decorators import secure_required
from app.models import User, Cliente
from app.serializers import UserSerializer, ClienteSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserCreate(mixins.CreateModelMixin,
                 generics.GenericAPIView):

    # queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = [
    #     permissions.AllowAny
    # ]

    @secure_required
    def post (self, request, *args, **kwargs):
        print('create')
        return self.create(request, *args, **kwargs)

class UserList(mixins.ListModelMixin,
               generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



# class ClienteViewSet(viewsets.ModelViewSet):
#     queryset = Cliente.objects.all()
#     serializer_class = ClienteSerializer

# @secure_required
# @ensure_csrf_cookie
def index(request):
    return render(request, 'app/index.html', {})