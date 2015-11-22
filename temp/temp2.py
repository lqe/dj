__author__ = 'lqe'

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj.settings")
django.setup()

from books.models import *
from home.models import *
from polls.models import *

'''
insert into student values('1234567899','student_name9');
('1234567891','student_name1'),
('1234567892','student_name2'),
('1234567893','student_name3'),
('1234567894','student_name4'),
('1234567895','student_name5'),
('1234567896','student_name6'),
('1234567897','student_name7'),
('1234567898','student_name8');

insert into course(cno,name,teacher_id) values
('1234567891','course_name1',NULL),
('1234567892','course_name2',NULL),
('1234567893','course_name3',NULL),
('1234567894','course_name4',NULL),
('1234567895','course_name5',NULL),
('1234567896','course_name6',NULL),
('1234567897','course_name7',NULL),
('1234567898','course_name8',NULL);

update course
set teacher_id = '1234567891'
where cno= '1234567891';

insert into teacher values
('1234567891','teacher_name1'),
('1234567892','teacher_name2'),
('1234567893','teacher_name3'),
('1234567894','teacher_name4'),
('1234567895','teacher_name5'),
('1234567896','teacher_name6'),
('1234567897','teacher_name7'),
('1234567898','teacher_name8');

insert into score(student_id, course_id)values
('1234567891','1234567891'),
('1234567892','1234567892'),
('1234567893','1234567893'),
('1234567894','1234567894'),
('1234567895','1234567895'),
('1234567896','1234567896'),
('1234567897','1234567897'),
('1234567898','1234567898');

select *
from student left join score
on sno = score.student_id;

select *
from student right join score
on sno = score.student_id;

select *
from student , score
where sno = score.student_id;

drop view if exists course_of_stu;
create view course_of_stu(student_id,student_name,course_id,course_name,teacher_id,teacher_name,grade) as
select sno, st.name, c.cno, c.name, wno, t.name, sc.grade
from student as st
left join  score as sc on st.sno = sc.student_id
left join course as c on sc.course_id = c.cno
left join teacher as t on c.teacher_id = t.wno;

'''


