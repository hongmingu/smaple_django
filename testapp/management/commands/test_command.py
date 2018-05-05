from django.core.management.base import BaseCommand, CommandError
from testapp.models import TestModel
import random


class Command(BaseCommand):
    help = 'help-text'

    def handle(self, *args, **options):
        TestModel.objects.create(number=random.randint(1, 1000))
