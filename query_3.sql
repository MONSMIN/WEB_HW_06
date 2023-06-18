SELECT g.name AS group_name, s.name AS subject_name, ROUND(AVG(gd.grade), 2) AS avg_grade
FROM groups g
JOIN students st ON g.id = st.group_id
JOIN grades gd ON st.id = gd.student_id
JOIN subjects s ON gd.subject_id = s.id
WHERE s.id = 7
GROUP BY g.id;

