# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0007_auto_20150831_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutuser',
            name='workout_target',
        ),
        migrations.AddField(
            model_name='workoutuser',
            name='series_target',
            field=models.PositiveIntegerField(default=30, help_text=b'Represents the target difficult for a workout series'),
        ),
    ]
