# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='pub_date',
            field=models.DateField(null=True),
        ),
    ]
