# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0006_auto_20150831_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='reps',
            field=models.PositiveIntegerField(help_text=b'Reps for repeating movements', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='set',
            name='seconds',
            field=models.PositiveIntegerField(help_text=b'Seconds to hold isometric movement', null=True, blank=True),
        ),
    ]
