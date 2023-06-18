SELECT g.name AS group_name, s.fullname AS students_name
FROM students s
JOIN groups g ON g.id  = s.group_id
WHERE s.group_id = 3;