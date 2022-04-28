from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer, ProjectSerializer, ToDoSerializer
from .filters import ProjectFilter, ToDoFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    filter_backends = (filters.DjangoFilterBackend,)
    # pagination_class = ProjectLimitOffsetPagination


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_class = ToDoFilter
    filter_backends = (filters.DjangoFilterBackend,)
    # pagination_class = ToDoLimitOffsetPagination

    def destroy(self, request, pk=None):
        todo = get_object_or_404(ToDo, pk=pk)
        if todo:
            todo.status = False
            todo.save()
        serializer = ToDoModelSerializer(todo)
        return Response(serializer.data)


def project_get(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)


def todo_get(request):
    todo = ToDo.objects.all()
    serializer = ToDoSerializer(todo, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)
