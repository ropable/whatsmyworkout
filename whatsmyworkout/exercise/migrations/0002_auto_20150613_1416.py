# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='desc',
            field=models.CharField(help_text=b'A short description of the exercise motion.', max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='isometric',
            field=models.BooleanField(default=False, help_text=b'An isometric exercise motion.'),
        ),
    ]
