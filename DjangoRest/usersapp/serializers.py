from rest_framework.serializers import HyperlinkedModelSerializer
from .models import myUser


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = myUser
        fields = ['username', 'first_name', 'last_name', 'email']
