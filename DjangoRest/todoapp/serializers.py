from dataclasses import fields
from rest_framework import serializers
from .models import Project, ToDo
from usersapp.serializers import UserModelSerializer, UserSerializer


class ProjectModelSerializer(serializers.ModelSerializer):
    # users = serializers.StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(serializers.ModelSerializer):
    # project = serializers.StringRelatedField()
    # user = serializers.StringRelatedField()
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    repo = serializers.CharField(max_length=128)
    users = UserSerializer(many=True)

class ToDoSerializer(serializers.Serializer):
    project = ProjectSerializer()
    user = UserSerializer()
