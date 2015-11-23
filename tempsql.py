# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Course(models.Model):
    cno = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=20)
    teacher = models.ForeignKey('Teacher', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FieldsLearning(models.Model):
    auto_field = models.AutoField(primary_key=True)
    uuid_field = models.CharField(max_length=32)
    binarg_field = models.TextField()
    char_field = models.CharField(max_length=512)
    text_field = models.TextField()
    boolean_field = models.IntegerField()
    null_boolean_field = models.IntegerField(blank=True, null=True)
    float_field = models.FloatField()
    small_integer_field = models.SmallIntegerField()
    integer_field = models.IntegerField()
    big_integer_field = models.BigIntegerField()
    positive_integer_field = models.IntegerField()
    positive_small_integer_field = models.SmallIntegerField()
    comma_separated_integer_field = models.CharField(max_length=512)
    date_field = models.DateField()
    time_field = models.TimeField()
    date_time_field = models.DateTimeField()
    duration_field = models.BigIntegerField()
    decimal_field = models.DecimalField(max_digits=9, decimal_places=2)
    email_field = models.CharField(max_length=254)
    url_field = models.CharField(max_length=200)
    file_field = models.CharField(max_length=100)
    image_field = models.CharField(max_length=100)
    file_path_field = models.CharField(max_length=100)
    ip_address_field = models.CharField(max_length=15)
    genericl_ip_address_field = models.CharField(max_length=39)
    slug_field = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'fields_learning'


class FieldsOption(models.Model):
    name = models.CharField(max_length=100)
    screen_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=254)
    year_in_school = models.CharField(max_length=2)
    regtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fields_option'


class Score(models.Model):
    grade = models.FloatField(blank=True, null=True)
    course = models.ForeignKey(Course)
    student = models.ForeignKey('Student')

    class Meta:
        managed = False
        db_table = 'score'


class Student(models.Model):
    sno = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'student'


class Teacher(models.Model):
    wno = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'teacher'