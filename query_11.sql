SELECT t.fullname AS teacher_name, s.fullname AS student_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM teachers t
JOIN subjects subj ON t.id = subj.teacher_id
JOIN grades g ON subj.id = g.subject_id
JOIN students s ON g.student_id = s.id
WHERE t.id = 5 AND s.id = 27;
