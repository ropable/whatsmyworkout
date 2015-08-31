# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0004_auto_20150829_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set',
            name='workout',
        ),
        migrations.AddField(
            model_name='workout',
            name='sets',
            field=models.ManyToManyField(to='workout.Set'),
        ),
        migrations.AlterField(
            model_name='workoutuser',
            name='exercise_target',
            field=models.PositiveIntegerField(default=2, help_text=b'Represents the typical difficulty of exercise assigned'),
        ),
        migrations.AlterField(
            model_name='workoutuser',
            name='set_target',
            field=models.PositiveIntegerField(default=10, help_text=b'Represents the target difficulty of a single set'),
        ),
        migrations.AlterField(
            model_name='workoutuser',
            name='workout_target',
            field=models.PositiveIntegerField(default=90, help_text=b'Represents the target difficult for a whole workout'),
        ),
    ]
