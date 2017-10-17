# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SN', models.CharField(max_length=30, verbose_name=b'\xe5\xba\x8f\xe5\x88\x97\xe5\x8f\xb7')),
                ('Business', models.CharField(max_length=100, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xb8\x9a\xe5\x8a\xa1')),
                ('IP', models.GenericIPAddressField(null=True, verbose_name=b'\xe5\x85\xac\xe7\xbd\x91IP', blank=True)),
                ('Inner_IP', models.GenericIPAddressField(null=True, verbose_name=b'\xe5\x86\x85\xe7\xbd\x91IP', blank=True)),
                ('User', models.CharField(max_length=30, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('Passwd', models.CharField(max_length=200, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('Port', models.CharField(max_length=30, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3')),
                ('Landing_mode', models.CharField(max_length=30, verbose_name=b'\xe7\x99\xbb\xe9\x99\x86\xe6\x96\xb9\xe5\xbc\x8f')),
                ('Create_Date', models.DateTimeField(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='cmdb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SN', models.CharField(max_length=30, verbose_name=b'\xe5\xba\x8f\xe5\x88\x97\xe5\x8f\xb7')),
                ('CPU', models.CharField(max_length=100, verbose_name=b'CPU')),
                ('Fan', models.CharField(max_length=100, verbose_name=b'\xe9\xa3\x8e\xe6\x89\x87')),
                ('Motherboard', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\xbb\xe6\x9d\xbf')),
                ('Memory', models.CharField(max_length=100, verbose_name=b'\xe5\x86\x85\xe5\xad\x98\xe6\x9d\xa1')),
                ('Graphics', models.CharField(max_length=100, verbose_name=b'\xe6\x98\xbe\xe5\x8d\xa1')),
                ('Hard_disk1', models.CharField(max_length=100, verbose_name=b'\xe7\xa1\xac\xe7\x9b\x981')),
                ('Hard_disk2', models.CharField(max_length=100, verbose_name=b'\xe7\xa1\xac\xe7\x9b\x982')),
                ('Keyboard', models.CharField(max_length=100, verbose_name=b'\xe9\x94\xae\xe7\x9b\x98')),
                ('Mouse', models.CharField(max_length=100, verbose_name=b'\xe9\xbc\xa0\xe6\xa0\x87')),
                ('Chassis', models.CharField(max_length=100, verbose_name=b'\xe6\x9c\xba\xe7\xae\xb1')),
                ('Power_Supply', models.CharField(max_length=100, verbose_name=b'\xe7\x94\xb5\xe6\xba\x90')),
                ('Monitor', models.CharField(max_length=100, verbose_name=b'\xe6\x98\xbe\xe7\xa4\xba\xe5\x99\xa8')),
                ('Who_uses', models.CharField(max_length=100, verbose_name=b'\xe4\xbd\xbf\xe7\x94\xa8\xe8\x80\x85')),
                ('Price', models.IntegerField(max_length=100, verbose_name=b'\xe9\x87\x87\xe8\xb4\xad\xe4\xbb\xb7')),
                ('Create_Date', models.DateTimeField(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='Group_Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Supplier_name', models.CharField(max_length=100, verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86')),
                ('Phone', models.IntegerField(max_length=100, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe6\x96\xb9\xe5\xbc\x8f')),
            ],
        ),
        migrations.AddField(
            model_name='cmdb',
            name='Supplier',
            field=models.ForeignKey(to='cmdb.Group_Supplier'),
        ),
        migrations.AddField(
            model_name='cmdb',
            name='dept',
            field=models.ForeignKey(blank=True, to='account.Dept', null=True),
        ),
    ]
