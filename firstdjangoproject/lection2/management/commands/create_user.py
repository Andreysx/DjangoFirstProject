from django.core.management.base import BaseCommand
from lection2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com', password='secret', age=25)
        # user = User(name='Andrey', email='andr@example.com', password='secret', age=27)
        user = User(name='Isaac', email='is@example.com', password='secret', age=28)
        user.save()
        self.stdout.write(f'{user}')
