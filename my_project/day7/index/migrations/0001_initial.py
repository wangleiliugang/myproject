# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-10-31 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30)),
                ('upass', models.CharField(max_length=30)),
                ('uemail', models.EmailField(max_length=254)),
            ],
        ),
    ]
