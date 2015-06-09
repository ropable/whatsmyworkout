from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import Truncator


@python_2_unicode_compatible
class ExerciseCategory(models.Model):
    """Describes the body focus area for different exercise motions.
    """
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Equipment(models.Model):
    """Describes basic pieces of equipment used for difference exercises.
    """
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Demo(models.Model):
    """A URL to a demonstration for how to correctly perform a single exercise.
    """
    url = models.URLField()
    description = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return Truncator(self.description).words(15)


@python_2_unicode_compatible
class Exercise(models.Model):
    """Describes a single exercise motion, with a relative difficulty.
    """
    name = models.CharField(max_length=256)
    difficulty = models.PositiveIntegerField()
    categories = models.ManyToManyField(ExerciseCategory, blank=True)
    equipment_req = models.ManyToManyField(Equipment, blank=True)
    demos = models.ManyToManyField(Demo, blank=True)

    def __str__(self):
        return self.name
