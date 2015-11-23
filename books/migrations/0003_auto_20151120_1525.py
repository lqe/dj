# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20151120_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTest1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
                'db_table': 'book_test1',
            },
        ),
        migrations.AlterModelTable(
            name='publisher',
            table='publisher',
        ),
    ]
