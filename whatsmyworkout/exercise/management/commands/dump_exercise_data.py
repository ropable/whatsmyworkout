from django.core.management.base import BaseCommand
from django.core import management


class Command(BaseCommand):
    help = 'Dumps current exercise app data to fixtures'

    def handle(self, *args, **options):
        for m in ['ExerciseCategory', 'Equipment', 'Demo', 'Exercise']:
            f = open('whatsmyworkout/exercise/fixtures/{}.json'.format(m.lower()), 'w')
            management.call_command('dumpdata', 'exercise.{}'.format(m), format='json', indent=4, stdout=f)
