SELECT grp.name AS group_name, s.fullname AS student_name,  g.grade AS grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects subj ON g.subject_id = subj.id
JOIN groups grp ON s.group_id = grp.id
WHERE grp.id = 3 AND subj.id = 7;
