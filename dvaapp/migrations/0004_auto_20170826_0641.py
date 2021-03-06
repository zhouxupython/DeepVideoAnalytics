# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0003_auto_20170826_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyzer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analyzer',
            name='mode',
            field=models.CharField(choices=[('T', 'Tensorflow'), ('C', 'Caffe'), ('P', 'Pytorch'), ('O', 'OpenCV')], db_index=True, default='T', max_length=1),
        ),
        migrations.AddField(
            model_name='detector',
            name='mode',
            field=models.CharField(choices=[('T', 'Tensorflow'), ('C', 'Caffe'), ('P', 'Pytorch'), ('O', 'OpenCV')], db_index=True, default='T', max_length=1),
        ),
        migrations.AddField(
            model_name='indexer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexer',
            name='mode',
            field=models.CharField(choices=[('T', 'Tensorflow'), ('C', 'Caffe'), ('P', 'Pytorch'), ('O', 'OpenCV')], db_index=True, default='T', max_length=1),
        ),
    ]
