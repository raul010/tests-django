from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import serializers, generics
from app.models import User, Cliente


# @ensure_csrf_cookie
class UserSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='account_detail',
        lookup_field='account_name'
    )
    users = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        lookup_field='username',
        many=True,
        read_only=False
    )


    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'password',)
        write_only_fields = ('password',)
        read_only_fields = ('id',)
        # lookup_field = 'username'


    def restore_object(self, attrs, instance=None):
        assert instance is None, 'Cannot update users with CreateUserSerializer'
        user = User(email=attrs['email'], username=attrs['username'])
        user.set_password(attrs['password'])
        return user




class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'idade')