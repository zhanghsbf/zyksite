# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('fan', models.ForeignKey(related_name='fan_user', to=settings.AUTH_USER_MODEL)),
                ('follow', models.ForeignKey(related_name='follow_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('is_boy', models.BooleanField()),
                ('note', models.TextField()),
                ('head_cut', models.ImageField(default='/media/head_cuts/default.jpg', upload_to='head_cuts')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
