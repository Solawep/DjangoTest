# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('DisplayUsers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200, default=datetime.datetime(2015, 12, 15, 20, 57, 39, 635611, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
