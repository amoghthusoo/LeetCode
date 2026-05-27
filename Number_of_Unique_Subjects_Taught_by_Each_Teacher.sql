select teacher_id, count(*) as cnt from
(select distinct teacher_id, subject_id from teacher) as t1
group by teacher_id;