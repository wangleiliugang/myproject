# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-10-28 03:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20201027_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='妻子')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('auth', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Author')),
            ],
        ),
    ]
