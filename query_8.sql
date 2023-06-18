SELECT t.fullname AS teacher_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM teachers t
JOIN subjects subj ON t.id = subj.teacher_id
JOIN grades g ON subj.id = g.subject_id
WHERE t.id = 5;
