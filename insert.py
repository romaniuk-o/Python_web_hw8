import psycopg2
from contextlib import contextmanager
from sqlite3 import Error
from faker import Faker
from random import randint
from datetime import datetime, timedelta

fake = Faker('uk-UA')



@contextmanager
def create_connection():
    """ create a database connection to a PostgreSQL database """
    conn = None
    try:
        conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='789123')
        print(conn)
        yield conn
        conn.commit()
    except Error as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


if __name__ == '__main__':
    # підготовка списку студентів та предметів
    students = []
    for _ in range(45):
        students.append(fake.name())
    subjects = ['web', 'data_science', 'english', 'SQL', 'goland']

    # інструкції наповнення таблиць
    sql_insert_groups_table = "INSERT INTO groups(id, gr_name) " \
                              "VALUES(1, 'first')," \
                                    "(2, 'second')," \
                                    "(3, 'third')"
    sql_insert_subject_table = "INSERT INTO subjects(id, subject, teacher) " \
                               "VALUES(1, 'goland', 'Romaniuk')," \
                                     "(2, 'web', 'Kuchma')," \
                                     "(3, 'data_science', 'Kalyna')," \
                                     "(4, 'SQL', 'Kuchma')," \
                                     "(5, 'english', 'Kalyna')"
    sql_insert_students_table = "INSERT INTO students(id, name, group_) VALUES(%s, %s, %s)"
    sql_insert_grades_table = "INSERT INTO grades(student, subject, grade, created_at) VALUES(%s, %s, %s, %s)"

    with create_connection() as conn:
        if conn is not None:
            cur = conn.cursor()
            cur.execute(sql_insert_groups_table)
            cur.execute(sql_insert_subject_table)
            for _ in range(0, 45):
                cur.execute(sql_insert_students_table, (_+1, students[randint(0, len(students)-1)], randint(1, 3)))

            for _ in range(0, 51):
                cur.execute(sql_insert_grades_table, (randint(1, len(students)-1),
                            randint(1, 5), randint(2, 5), datetime.now()))
            cur.close()
        else:
            print('Error: can\'t create the database connection')
