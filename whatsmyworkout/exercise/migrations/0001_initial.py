# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('description', models.CharField(max_length=512, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('difficulty', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='categories',
            field=models.ManyToManyField(to='exercise.ExerciseCategory', blank=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='demos',
            field=models.ManyToManyField(to='exercise.Demo', blank=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='equipment_req',
            field=models.ManyToManyField(to='exercise.Equipment', blank=True),
        ),
    ]
