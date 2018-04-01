# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo1',
            field=models.ImageField(upload_to='photo/%Y/%m/%d', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='photo2',
            field=models.ImageField(upload_to='photo/%Y/%m/%d', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='photo3',
            field=models.ImageField(upload_to='photo/%Y/%m/%d', null=True, blank=True),
        ),
    ]
