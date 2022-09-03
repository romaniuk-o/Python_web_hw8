from insert import create_connection

# 5 студентів із найбільшим середнім балом з усіх предметів.
sql1 = """
SELECT s.name, round(avg(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 5
"""


# 1 студент із найвищим середнім балом з одного предмета.
sql2 = """
SELECT sb.subject, s.name, round(avg(g.grade), 2) as grade
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN subjects sb ON sb.id = g.subject
WHERE sb.id = 1
GROUP BY s.id, sb.id
ORDER BY grade DESC
LIMIT 1
"""
# середній бал в групі по одному предмету.
sql3 = """
SELECT sb.subject, gr.gr_name, round(avg(g.grade), 2) as grade
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN subjects sb ON sb.id = g.subject
LEFT JOIN "groups" gr ON gr.id = s.group_
WHERE sb.id = 1
GROUP BY sb.subject, gr.id
ORDER BY grade DESC
"""
# Середній бал у потоці.
sql4 = """
SELECT  round(avg(g.grade), 2) as grade
FROM grades g
"""
# Які курси читає викладач.
sql5 = """
SELECT sb.teacher, sb.subject as list_of_subjects
FROM subjects sb
WHERE sb.teacher = 'Kalyna'
"""
# Список студентів у групі.
sql6 = """
SELECT s.name, gr.gr_name as group_number
FROM students s
LEFT JOIN "groups" gr ON gr.id = s.group_
WHERE gr.id = 1
GROUP BY s.name, gr.gr_name
ORDER BY s.name DESC
"""
# Оцінки студентів у групі з предмета.
sql7 = """
SELECT s.name, gr.gr_name, sb.subject, g.grade 
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN "groups" gr ON gr.id = s.group_   
LEFT JOIN subjects sb ON sb.id = g.subject 
WHERE sb.id = 2 and gr.id = 2
GROUP BY s.name, gr.gr_name, sb.subject, g.grade
ORDER BY s.name DESC
"""
# Оцінки студентів у групі з предмета на останньому занятті.
sql8 = """
SELECT s.name, gr.gr_name, sb.subject, g.grade, g.created_at
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN "groups" gr ON gr.id = s.group_   
LEFT JOIN subjects sb ON sb.id = g.subject 
WHERE sb.id = 4 and gr.id = 1 and g.created_at = (
    SELECT g.created_at
    FROM grades g
    LEFT JOIN students s ON s.id = g.student
    LEFT JOIN "groups" gr ON gr.id = s.group_ 
    WHERE g.subject = 4 and gr.id = 1
    ORDER BY g.created_at DESC
    LIMIT 1
    )
ORDER BY s.name DESC
"""
# Список курсів, які відвідує студент.
sql9 = """
SELECT s.name, sb.subject
FROM grades g
LEFT JOIN students s ON s.id = g.student 
LEFT JOIN subjects sb ON sb.id = g.subject 
WHERE g.student = 32 
"""
# Список курсів, які студенту читає викладач.
sql10 = """
SELECT sb.subject, sb.teacher, s.name
FROM grades g
LEFT JOIN subjects sb ON sb.id = g.subject 
LEFT JOIN students s ON s.id = g.student
WHERE g.student = 18 and sb.teacher = 'Kuchma'
"""
# Середній бал, який викладач ставить студенту.
sql11 = """
SELECT sb.teacher, s.name, round(avg(g.grade), 2) as grade
FROM grades g
LEFT JOIN students s ON s.id = g.student
LEFT JOIN subjects sb ON sb.id = g.subject 
WHERE g.student = 18 and sb.teacher = 'Kuchma'
GROUP BY sb.teacher, s.name
"""
# Середній бал, який ставить викладач.
sql12 = """
SELECT sb.teacher, SUM(g.grade), COUNT(g.grade), round(avg(g.grade), 2) as grade
FROM grades g
LEFT JOIN subjects sb ON sb.id = g.subject 
WHERE sb.teacher = 'Kuchma'
GROUP BY sb.teacher
"""
sql_list = [sql1, sql2, sql3, sql4, sql5, sql6, sql7, sql8, sql9, sql10, sql11, sql12]
def asker(sql):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


if __name__ == '__main__':
    for _ in sql_list:
        print(asker(_))
        print(input(f'press any key to continue---->  '))