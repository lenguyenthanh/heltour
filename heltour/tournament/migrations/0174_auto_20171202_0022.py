# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-12-02 00:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import select2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0173_set_document_owners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='owner',
            field=select2.fields.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
