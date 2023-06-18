SELECT st.fullname  AS students_name, subj.name  AS subjects_name
FROM students st
JOIN grades g ON g.student_id = st.id 
JOIN subjects subj ON subj.id = g.subject_id
WHERE st.id  = 27
GROUP BY subj.id;