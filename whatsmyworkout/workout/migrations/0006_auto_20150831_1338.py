# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0005_auto_20150831_1314'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='set',
            unique_together=set([('exercise', 'reps'), ('exercise', 'seconds')]),
        ),
    ]
