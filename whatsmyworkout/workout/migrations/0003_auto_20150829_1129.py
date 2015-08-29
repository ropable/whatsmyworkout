# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_auto_20150621_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutuser',
            name='set_target',
            field=models.PositiveIntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='workoutuser',
            name='exercise_target',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='workoutuser',
            name='workout_target',
            field=models.PositiveIntegerField(default=135),
        ),
    ]
