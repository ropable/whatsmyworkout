from django.db import models


class ExerciseCategory(models.Model):
    name = models.CharField(max_length=256)


class Equipment(models.Model):
    name = models.CharField(max_length=256)


class Demo(models.Model):
    url = models.URLField()


class Exercise(models.Model):
    name = models.CharField(max_length=256)
    difficulty = models.PositiveIntegerField()
    categories = models.ManyToManyField(ExerciseCategory, blank=True)
    equipment_req = models.ManyToManyField(Equipment, blank=True)
    demos = models.ManyToManyField(Demo, blank=True)
