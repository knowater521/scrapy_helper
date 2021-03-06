# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 13:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('alias', models.CharField(max_length=200)),
                ('domain', models.CharField(max_length=100)),
                ('start_urls', models.TextField()),
                ('user_agents', models.TextField(default='text')),
                ('pipelines', models.CharField(choices=[(1, 'JsonExportPipeline'), (2, 'CsvExportPipeline')], max_length=100)),
                ('download_delay', models.IntegerField(default=3)),
                ('status', models.CharField(choices=[(0, '\u521d\u59cb\u5316'), (1, '\u8fd0\u884c'), (2, '\u505c\u6b62')], default=0, max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=256)),
                ('callback_func', models.CharField(max_length=50, verbose_name='\u56de\u8c03')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Project')),
            ],
        ),
        migrations.AddField(
            model_name='field',
            name='rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Rule'),
        ),
    ]
