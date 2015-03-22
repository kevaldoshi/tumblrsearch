# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=200)),
                ('url', models.URLField(unique=True, max_length=250, verbose_name=b'A Tumblr Blog URL', validators=[django.core.validators.URLValidator()])),
                ('pub_date', models.DateTimeField()),
                ('img_url', models.URLField(unique=True, max_length=250, verbose_name=b'A Tumblr Blog Image URL', validators=[django.core.validators.URLValidator()])),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
