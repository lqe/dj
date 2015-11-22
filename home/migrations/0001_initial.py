# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FiledsRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'fileds_relationship',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cno', models.CharField(max_length=10, serialize=False, verbose_name='\u5b66\u53f7', primary_key=True, db_column=b'wno')),
                ('name', models.CharField(max_length=20, verbose_name='\u8bfe\u7a0b\u540d', db_index=True)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='FieldsOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, db_column=b'name', db_index=True)),
                ('screen_name', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'm', b'Man'), (b'f', b'Female')])),
                ('email', models.EmailField(max_length=254, db_tablespace=b'email_index', db_index=True)),
                ('year_in_school', models.CharField(default=b'FR', max_length=2, verbose_name='\u5e74\u7ea7', choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')])),
                ('regtime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'fields_option',
            },
        ),
        migrations.CreateModel(
            name='FieldsType',
            fields=[
                ('auto_field', models.AutoField(serialize=False, primary_key=True)),
                ('uuid_field', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('binarg_field', models.BinaryField()),
                ('char_field', models.CharField(max_length=512)),
                ('text_field', models.TextField()),
                ('boolean_field', models.BooleanField()),
                ('null_boolean_field', models.NullBooleanField()),
                ('float_field', models.FloatField()),
                ('small_integer_field', models.SmallIntegerField()),
                ('integer_field', models.IntegerField()),
                ('big_integer_field', models.BigIntegerField()),
                ('positive_integer_field', models.PositiveIntegerField()),
                ('positive_small_integer_field', models.PositiveSmallIntegerField()),
                ('comma_separated_integer_field', models.CommaSeparatedIntegerField(max_length=512)),
                ('date_field', models.DateField(auto_now=True)),
                ('time_field', models.TimeField(auto_now=datetime.datetime.now)),
                ('date_time_field', models.DateTimeField(auto_now_add=True)),
                ('duration_field', models.DurationField()),
                ('decimal_field', models.DecimalField(max_digits=9, decimal_places=2)),
                ('email_field', models.EmailField(max_length=254)),
                ('url_field', models.URLField()),
                ('file_field', models.FileField(upload_to=b'files/%Y/%m/%d')),
                ('image_field', models.ImageField(height_field=100, width_field=100, upload_to=b'/upload_to/images')),
                ('file_path_field', models.FilePathField(path=b'/upload_to/images', recursive=True, match=b'.*.jpg')),
                ('ip_address_field', models.IPAddressField()),
                ('genericl_ip_address_field', models.GenericIPAddressField()),
                ('slug_field', models.SlugField()),
            ],
            options={
                'db_table': 'fields_learning',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.FloatField()),
                ('course', models.ForeignKey(to='home.Course')),
            ],
            options={
                'db_table': 'score',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.CharField(max_length=10, serialize=False, verbose_name='\u5b66\u53f7', primary_key=True, db_column=b'sno')),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d', db_index=True)),
                ('cno', models.ManyToManyField(to='home.Course', through='home.Score')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('wno', models.CharField(max_length=10, serialize=False, verbose_name='\u5b66\u53f7', primary_key=True, db_column=b'wno')),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d', db_index=True)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.AddField(
            model_name='score',
            name='student',
            field=models.ForeignKey(to='home.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(related_query_name=b'courses', related_name='teached_by', on_delete=django.db.models.deletion.SET_NULL, to='home.Teacher', null=True),
        ),
    ]
