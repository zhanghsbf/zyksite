# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonghu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_boy',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='note',
            field=models.TextField(null=True, blank=True),
        ),
    ]
