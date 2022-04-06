from rest_framework.viewsets import ModelViewSet
from .models import myUser
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = myUser.objects.all()
    serializer_class = UserModelSerializer
