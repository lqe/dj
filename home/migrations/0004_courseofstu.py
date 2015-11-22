# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20151122_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseOfStu',
            fields=[
                ('student', models.ForeignKey(primary_key=True, serialize=False, to='home.Student')),
                ('student_name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('course_name', models.CharField(max_length=20, verbose_name='\u8bfe\u7a0b\u540d')),
                ('teacher_name', models.CharField(max_length=20, verbose_name='\u6559\u8bfe\u8001\u5e08\u59d3\u540d')),
                ('grade', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'course_of_stu',
                'managed': False,
            },
        ),
    ]
