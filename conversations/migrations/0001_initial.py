# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-17 04:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('pub_date', models.DateField()),
                ('sender_id', models.IntegerField()),
                ('mtm', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterOrderWithRespectTo(
            name='messages',
            order_with_respect_to='pub_date',
        ),
    ]
