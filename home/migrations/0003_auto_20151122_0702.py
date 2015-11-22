# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20151122_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(related_query_name=b'courses', related_name='teached_by', on_delete=django.db.models.deletion.SET_NULL, default=None, to='home.Teacher', null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='grade',
            field=models.FloatField(null=True),
        ),
    ]
