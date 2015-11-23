# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cno',
            field=models.CharField(max_length=10, serialize=False, verbose_name='\u5b66\u53f7', primary_key=True, db_column=b'cno'),
        ),
    ]
