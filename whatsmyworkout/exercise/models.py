from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import Truncator


@python_2_unicode_compatible
class ExerciseCategory(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return name


@python_2_unicode_compatible
class Equipment(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return name


@python_2_unicode_compatible
class Demo(models.Model):
    url = models.URLField()
    description = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return Truncator(self.description).words(15)


@python_2_unicode_compatible
class Exercise(models.Model):
    name = models.CharField(max_length=256)
    difficulty = models.PositiveIntegerField()
    categories = models.ManyToManyField(ExerciseCategory, blank=True)
    equipment_req = models.ManyToManyField(Equipment, blank=True)
    demos = models.ManyToManyField(Demo, blank=True)

    def __str__(self):
        return name
