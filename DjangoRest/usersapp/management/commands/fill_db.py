from django.core.management.base import BaseCommand
from usersapp.models import myUser
from django.contrib.auth.models import User

import json, os

JSON_PATH = 'usersapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json('users')
        myUser.objects.all().delete()
        for user in users:
            new_user = myUser(**user)
            new_user.save()

        myUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)
        