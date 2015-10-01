# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('jitterbunk', '0004_bunk_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunk',
            name='from_user',
            field=models.ForeignKey(related_name='from_bunk', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bunk',
            name='to_user',
            field=models.ForeignKey(related_name='to_bunk', to=settings.AUTH_USER_MODEL),
        ),
    ]
