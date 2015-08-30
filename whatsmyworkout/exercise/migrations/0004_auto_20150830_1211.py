# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_exercise_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo',
            name='url',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(unique=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(unique=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='exercisecategory',
            name='name',
            field=models.CharField(unique=True, max_length=256),
        ),
    ]
