# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0004_auto_20150830_1211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipment',
            options={'verbose_name_plural': 'equipment'},
        ),
        migrations.AlterModelOptions(
            name='exercisecategory',
            options={'verbose_name_plural': 'exercise categories'},
        ),
    ]
