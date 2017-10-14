# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('contactperson', models.CharField(max_length=50, null=True)),
                ('contactphone', models.CharField(max_length=50, null=True)),
                ('contactemail', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='idclist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idcname', models.CharField(max_length=50)),
                ('idclevel', models.IntegerField(max_length=11, null=True)),
                ('idcdesc', models.CharField(max_length=255)),
                ('idcaddr', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='servers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=100)),
                ('externalip', models.CharField(max_length=150)),
                ('internalip', models.CharField(max_length=150)),
                ('virtip', models.CharField(max_length=150)),
                ('passwd', models.CharField(max_length=150)),
                ('cpu', models.CharField(max_length=50, null=True)),
                ('cpumhz', models.CharField(max_length=50, null=True)),
                ('mem', models.CharField(max_length=50, null=True)),
                ('disk', models.CharField(max_length=50, null=True)),
                ('type', models.IntegerField(max_length=11, null=True)),
                ('status', models.IntegerField(default=3, max_length=11, null=True)),
                ('system', models.IntegerField(max_length=11, null=True)),
                ('addtime', models.DateTimeField(auto_now_add=True, null=True)),
                ('comment', models.TextField(max_length=500, null=True, blank=True)),
                ('businessname', models.ForeignKey(blank=True, to='serversys.business', null=True)),
                ('dept', models.ForeignKey(blank=True, to='account.Dept', null=True)),
                ('idc', models.ForeignKey(blank=True, to='serversys.idclist', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'\xe5\x8c\x97\xe4\xba\xac', max_length=50)),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='idclist',
            name='idczone',
            field=models.ForeignKey(blank=True, to='serversys.zone', null=True),
        ),
    ]
