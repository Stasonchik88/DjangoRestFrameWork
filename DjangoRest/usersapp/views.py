from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from .models import myUser
from .serializers import UserModelSerializer, UserSerializer


class UserModelViewSet(ModelViewSet):
    queryset = myUser.objects.all()
    serializer_class = UserModelSerializer


def user_get(request, pk=None):
    if pk is None:
        users = myUser.objects.all()
        serializer = UserSerializer(users, many=True)
    else:
        author = myUser.objects.get(pk=pk)
        serializer = UserSerializer(author)

    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)
