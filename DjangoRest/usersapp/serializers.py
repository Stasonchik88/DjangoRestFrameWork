from rest_framework.serializers import Serializer, HyperlinkedModelSerializer, CharField, EmailField, ValidationError
from .models import myUser


class UserSerializer(Serializer):
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    email = EmailField(max_length=100)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    def create(self, validated_data):
        user = myUser(**validated_data)
        user.save()
        return user


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = myUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
