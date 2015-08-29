# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_exercise_image'),
        ('workout', '0003_auto_20150829_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reps', models.PositiveIntegerField(help_text=b'Reps for repeating movements', blank=True)),
                ('seconds', models.PositiveIntegerField(help_text=b'Seconds to hold isometric movement', blank=True)),
                ('exercise', models.ForeignKey(to='exercise.Exercise')),
            ],
        ),
        migrations.RemoveField(
            model_name='activity',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='workout',
        ),
        migrations.RenameField(
            model_name='workout',
            old_name='sets',
            new_name='repeats',
        ),
        migrations.AlterField(
            model_name='workoutuser',
            name='exercise_target',
            field=models.PositiveIntegerField(default=3, help_text=b'Represents the typical difficulty of exercise assigned'),
        ),
        migrations.AlterField(
            model_name='workoutuser',
            name='set_target',
            field=models.PositiveIntegerField(default=15, help_text=b'Represents the target difficulty of a single set'),
        ),
        migrations.AlterField(
            model_name='workoutuser',
            name='workout_target',
            field=models.PositiveIntegerField(default=135, help_text=b'Represents the target difficult for a whole workout'),
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.AddField(
            model_name='set',
            name='workout',
            field=models.ForeignKey(to='workout.Workout'),
        ),
    ]
