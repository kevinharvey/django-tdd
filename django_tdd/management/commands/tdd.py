from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *apps, **options):
        from django.core.management import call_command
        from django.conf import settings

        # runserver complains if this setting is not set
        settings.ALLOWED_HOSTS += 'localhost'
        call_command('test')
        call_command('runserver')
