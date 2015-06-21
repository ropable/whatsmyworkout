# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutuser',
            name='exercise_target',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='workoutuser',
            name='workout_target',
            field=models.PositiveIntegerField(default=300),
        ),
    ]
