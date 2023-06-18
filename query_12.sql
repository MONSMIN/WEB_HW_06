SELECT s.fullname AS student_name, grp.name AS group_name, subj.name AS subjects_name, g.date_of AS last_date, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects subj ON g.subject_id = subj.id
JOIN groups grp ON s.group_id = grp.id
WHERE subj.id = 7 
AND grp.id  = 3 
AND g.date_of = 
	(
    SELECT MAX(date_of)
    FROM grades
    WHERE subject_id = 7
    );