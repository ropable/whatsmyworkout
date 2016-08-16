from django.core.management.base import BaseCommand
from django.core import management


class Command(BaseCommand):
    help = 'Loads current exercise app data from fixtures'

    def handle(self, *args, **options):
        for m in ['exercisecategory', 'equipment', 'demo', 'exercise']:
            management.call_command('loaddata', 'whatsmyworkout/exercise/fixtures/{}.json'.format(m))
