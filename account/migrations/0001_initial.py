# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=40, db_index=True)),
                ('email', models.EmailField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('nickname', models.CharField(max_length=64, null=True)),
                ('sex', models.CharField(default=2, max_length=2, null=True)),
                ('role', models.IntegerField(default=1, max_length=40)),
                ('phone', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'\xe8\xbf\x90\xe7\xbb\xb4\xe9\x83\xa8', unique=True, max_length=80)),
                ('comment', models.CharField(max_length=160, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='dept',
            field=models.ForeignKey(blank=True, to='account.Dept', null=True),
        ),
    ]
