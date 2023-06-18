SELECT s.name AS subject_name, t.fullname AS teacher
FROM subjects s
JOIN teachers t ON s.teacher_id = t.id 
WHERE t.id = 5
;