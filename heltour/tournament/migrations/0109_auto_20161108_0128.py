# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-08 01:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0108_league_time_control'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeagueNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('mod', 'Moderation stream')], max_length=255)),
                ('slack_channel', models.CharField(max_length=255)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.League')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='leaguenotification',
            unique_together=set([('league', 'slack_channel', 'type')]),
        ),
    ]
