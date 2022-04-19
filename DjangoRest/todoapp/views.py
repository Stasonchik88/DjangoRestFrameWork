from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer, ProjectSerializer, ToDoSerializer


class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


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
