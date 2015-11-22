#-*- coding:utf-8 -*-
from django.db import models

class HomeAppRouter(object):
    pass

class FieldsOption(models.Model):
    '''
    null=False. if True, Django will store empty values as NULL in the database.
    blank=False, if True, the field is allowed to be blank.
    default.
        This can be a value or a callable object.
        The default cannot be a mutable object (model instance, list, set, etc.),
        as a reference to the same instance of that object would be used as the default value in all new model instances.
    primary_key=False.
        If True, this field is the primary key for the model. and implying null=False and unique=True.
        Only one primary key is allowed on an object. and the primary key field is read-only.
        If you change the value of the primary key on an existing object and then save it,\
        a new object will be created alongside the old one.
    unique=False
        If True, this field must be unique throughout the table.
        If you try to save a model with a duplicate value in a unique field, \
        a django.db.IntegrityError will be raised by the model’s save() method.
        When unique is True, you don’t need to specify db_index, because unique implies the creation of an index.
        This option is valid on all field types except ManyToManyField, OneToOneField, and FileField.
    db_column. The name of the database column to use for this field.
    db_index=False. if True, If True, django-admin sqlindexes will output a CREATE INDEX statement for this field.
    db_tablespace. The name of the database tablespace to use for this field’s index, if this field is indexed.
    verbose_name.
        A human-readable name for the field.
        If the verbose name isn’t given, Django will automatically create it \
        using the field’s attribute name, converting underscores to spaces.
    validators.
        A list of validators to run for this field. See the validators documentation for more information.
    error_messages.
        The error_messages argument lets you override the default messages that the field will raise.
        Pass in a dictionary with keys matching the error messages you want to override.
    help_text
        Extra “help” text to be displayed with the form widget.
        It’s useful for documentation even if your field isn’t used on a form.
        you can use plain text and django.utils.html.escape() to escape any HTML special characters,
        Ensure that you escape any help text that may come from untrusted users to avoid a cross-site scripting attack.
    unique_for_date.
        Set this to the name of a DateField or DateTimeField to require that \
        this field be unique for the value of the date field.
        if you have a field title that has unique_for_date="pub_date", \
        then Django wouldn’t allow the entry of two records with the same title and pub_date.
    unique_for_month
    unique_for_year
    '''
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    name = models.CharField(max_length=100, db_index=True, db_column='name')
    screen_name = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=1, choices=[('m','Man'),('f','Female')])
    email = models.EmailField(db_index=True, db_tablespace='email_index')
    year_in_school = models.CharField(max_length=2,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=FRESHMAN,
                                      verbose_name=u'年级')
    regtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'fields_option'

    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        if self.screen_name == '':
            self.screen_name = None
        models.Model.save(self, **kwargs)

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)

class FieldsType(models.Model):

    #一个IntegerField 根据实际ID自动增长
    auto_field = models.AutoField(primary_key=True)

    # unique identifiers.  a good alternative to autoField for primary_key.
    # the database will not generate the uuid for , so it is recommended to use default
    # When used on PostgreSQL, this stores in a uuid datatype, otherwise in a char(32)
    import uuid
    uuid_field = models.UUIDField(default=uuid.uuid4, editable=False)

    # 这是一个用来存储原始二进制码的Field. 只支持bytes 声明
    binarg_field = models.BinaryField()

    # class CharField(max_length=None[, **options])¶
    # 必填参数中max_length.  from widget:TextInput
    char_field = models.CharField(max_length=512)
    # a large text field. form widget:Textarea
    text_field = models.TextField()

    # 一个 true/false 字段。
    # 此字段的默认表单挂件是一个CheckboxInput.
    boolean_field = models.BooleanField()
    # Like a BooleanField, but allows NULL as one of the options.
    # 如果Field.default没有指定的话， BooleanField 的默认值是 None
    # Use this instead of a BooleanField with null=True.
    null_boolean_field = models.NullBooleanField()

    # A floating-point number represented in Python by a float instance.
    float_field = models.FloatField()
    # Values from -32768 to 32767
    small_integer_field = models.SmallIntegerField()
    # values from  -2147483648 to 2147483647 are safe in all databases。
    integer_field = models.IntegerField()
    # 64位整数 values from -9223372036854775808 to 9223372036854775807之间.
    # default form widget:TextInput.
    big_integer_field = models.BigIntegerField()
    # Values from 0 to 2147483647 are safe in all databases supported by Django.
    positive_integer_field = models.PositiveIntegerField()
    # Values from 0 to 32767 are safe in all databases supported by Django.
    positive_small_integer_field = models.PositiveSmallIntegerField()
    # class CommaSeparatedIntegerField(max_length=None[, **options])¶
    # A field of integers separated by commas. 一个逗号分隔的整数字段。像 CharField一样， 需要一个max_length 参数
    comma_separated_integer_field = models.CommaSeparatedIntegerField(max_length=512)


    # class DateField([auto_now=False, auto_now_add=False, **options])¶
    # represented in python by a datetime.time instance
    # auto_now. Automatically set the field to now every time the object is saved.
    # auto_now_add. Automatically set the field to now when the object is first created.
    # from widget:TextInput
    # 在目前的实现中，设置auto_now或者auto_now_add为True将为让这个字段同时得到editable=False和blank=True这两个设置.
    import datetime
    date_field = models.DateField(auto_now=datetime.datetime.now)
    #class TimeField([auto_now=False, auto_now_add=False, **options])
    time_field = models.TimeField(auto_now=datetime.datetime.now)
    # class DateTimeField([auto_now=False, auto_now_add=False, **options])¶
    # A date and time, represented in Python by a datetime.datetime instance.
    # form widget:TextInput
    date_time_field = models.DateTimeField(auto_now_add=datetime.datetime.now)
    # A field for storing periods of time - modeled in Python by timedelta.
    # When used on PostgreSQL, the data type used is an interval and
    # on Oracle the data type is INTERVAL DAY(9) TO SECOND(6).
    # Otherwise a bigint of microseconds is used.
    duration_field = models.DurationField()

    # class DecimalField(max_digits=None, decimal_places=None[, **options])¶
    # A fixed-precision decimal number, represented in Python by a Decimal instance.
    # max_digits. The maximum number of digits allowed in the number. this number must be >= decimal_places.
    # decimal_places. The number of decimal places to store with the number.
    decimal_field = models.DecimalField(max_digits=9, decimal_places=2)



    # class EmailField([max_length=254, **options])
    # A CharField that checks that the value is a valid email address.
    # It uses EmailValidator to validate the input.
    # The default max_length was increased from 75 to 254 in order to be compliant with RFC3696/5321.
    email_field = models.EmailField()

    # if you don't specify max_length , a default of 200 is used
    # the default form widget for this field is a TextInput
    url_field = models.URLField() # class URLField([max_length=200, **options])¶


    # class FileField([upload_to=None, max_length=100, **options])¶.
    # upload_to may contain strftime() formatting, which will be replaced by the date/time of the file upload.
    # When you access a FileField on a model,
    # you are given an instance of FieldFile as a proxy for accessing the underlying file.
    # In addition to the functionality inherited from django.core.files.File,
    # this class has several attributes and methods that can be used to interact with file data:
    # FieldFile.url, FieldFile.open(mode='rb'), FieldFile.close(),
    # FieldFile.save(name, content, save=True), FieldFile.delete(save=True)
    # default form wedget:ClearableFileInput.
    file_field = models.FileField(upload_to='files/%Y/%m/%d')
    # class ImageField([upload_to=None, height_field=None, width_field=None, max_length=100, **options])¶
    # In addition to the special attributes that are available for FileField,
    # an ImageField also has height and width attributes.
    image_field = models.ImageField(upload_to='/upload_to/images',height_field=100, width_field=100)
    # class FilePathField(path=None[, match=None, recursive=False, max_length=100, **options])¶
    # FilePathField instances are created in database as varchar columns
    # recursive. specifies whether all subdirectories of path should be included
    # allow_files. specifies whether files in the specified location should be included. default True
    # allow_folders. specifies whether folders in the specified location should be included. default False
    # Either this or allow_folders must be True.
    file_path_field = models.FilePathField(path='/upload_to/images', match='.*.jpg', recursive=True)

    # Deprecated since version 1.7. so use GenericIPAddressField instead of it.
    # form widget:TextInput.
    ip_address_field = models.IPAddressField()
    # class GenericIPAddressField([protocol=both, unpack_ipv4=False, **options])¶
    # An IPv4 or IPv6 address, in string format (e.g. 192.0.2.30 or 2a02:42fe::4).
    # form widget:TextInput.
    genericl_ip_address_field = models.GenericIPAddressField()

    slug_field = models.SlugField() # class SlugField([max_length=50, **options])¶


    class Meta:
        db_table='fields_learning'

# teacher 1:n course
# student n:n course

class Course(models.Model):
    cno = models.CharField(verbose_name=u'学号', max_length=10, primary_key=True, db_column='cno')
    name = models.CharField(verbose_name=u'课程名', max_length=20, db_index=True)
    teacher = models.ForeignKey('Teacher',
                                to_field='wno',
                                related_name='courses',
                                related_query_name='my_course',
                                null=True,
                                default=None,
                                on_delete=models.SET_NULL)

    class Meta:
        db_table='course'

    def __unicode__(self):
        return self.name

class Student(models.Model):
    sno = models.CharField(verbose_name=u'学号', max_length=10, primary_key=True, db_column='sno')
    name = models.CharField(verbose_name=u'姓名', max_length=20, db_index=True)
    cno = models.ManyToManyField(Course,
                                 through='Score',
                                 through_fields=('student','course'),
                                 )

    class Meta:
        db_table='student'

    def __unicode__(self):
        return self.name

class Score(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    grade = models.FloatField(null=True)

    class Meta:
        db_table='score'

    def __unicode__(self):
        return '%s select course<%s> . grade is %s' % (self.student.name, self.course.name, str(self.grade or 'NULL'))

class Teacher(models.Model):
    wno = models.CharField(verbose_name=u'学号', max_length=10, primary_key=True, db_column='wno')
    name = models.CharField(verbose_name=u'姓名', max_length=20, db_index=True)

    class Meta:
        db_table='teacher'

    def __unicode__(self):
        return self.name

class CourseOfStu(models.Model):
    student = models.ForeignKey(Student, primary_key=True)
    student_name = models.CharField(verbose_name=u'姓名', max_length=20)
    course = models.ForeignKey(Course, null=True)
    course_name = models.CharField(verbose_name=u'课程名', max_length=20)
    teacher = models.ForeignKey(Teacher, null=True)
    teacher_name = models.CharField(verbose_name=u'教课老师姓名', max_length=20)
    grade = models.FloatField(null=True)

    class Meta:
        managed = False
        db_table='course_of_stu'


class FiledsRelationship(models.Model):
    '''
    ForeignKey:
        多对一关系. 需要一个位置参数：与该模型关联的类.
        创建一个递归关系– 一个对象和它自己是多对一的关系 – 使用models.ForeignKey('self').
        如果你需要对一个还没有被定义的模型(model)创建关系, 你可以在创建关系时使用该模型的名字, 而不是该模型的对象本身:
    '''
    class Meta:
        managed = False
        db_table = 'fileds_relationship'

if __name__ == '__main__':
    student = Student.objects.first()
    course = Course.objects.first()
    teacher = Teacher.objects.first()

    # 获取课程course的教师
    teacher = course.teacher
    # 获取教课程名称为course_开头的所有老师
    teachers = Teacher.objects.filter(my_course__name__startswith = 'course_')
    # 获取student的所有老师
    teachers = (course.teacher for course in Course.objects.filter(student=student))


    # 获取学生student所有的课
    courses = student.cno.all()
    # 获取学生student所有课的成绩
    scores = student.score_set.all()

    # 获取选course的学生
    students = course.student_set.all()
    # 获取选course的学生的成绩
    scores = student.score_set.all()

    # 获取老师的所有课程
    courses = teacher.courses.all()


    





