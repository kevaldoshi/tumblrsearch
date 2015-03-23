# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20150323_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='caption',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
    ]
