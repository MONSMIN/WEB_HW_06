SELECT subj.name AS subjects_name, s.fullname AS student_name, t.fullname AS teacher_name 
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects subj ON g.subject_id = subj.id
JOIN teachers t ON subj.teacher_id = t.id
WHERE s.id = 27 AND t.id = 5
GROUP BY subj.name;
