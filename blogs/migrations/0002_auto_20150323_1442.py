# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img_url',
            field=models.URLField(max_length=250, verbose_name=b'A Tumblr Blog Image URL', validators=[django.core.validators.URLValidator()]),
            preserve_default=True,
        ),
    ]
