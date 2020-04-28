from django.core.management.base import BaseCommand

class Command(BaseCommand):  # Стандартное оформление команд. Менять нельзя.

    def handle(self, *args, **options):  # Стандартное оформление команд. Менять нельзя.
        print('Hello')