import psycopg2
from contextlib import contextmanager
from sqlite3 import Error


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
    sql_create_groups = """CREATE TABLE IF NOT EXISTS groups (
        id SERIAL PRIMARY KEY,
        gr_name VARCHAR(120)
);"""

    sql_create_subject_table = """CREATE TABLE IF NOT EXISTS subjects (
        id SERIAL PRIMARY KEY,
        subject VARCHAR(120),
        teacher VARCHAR(120)
        );"""

    sql_create_students_table = """CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(120),
            group_ INTEGER REFERENCES groups(id)
        ); """
    sql_create_grades_table = """CREATE TABLE IF NOT EXISTS grades (
        student integer REFERENCES students(id),
        subject integer REFERENCES subjects(id),
        grade integer,
        created_at timestamp
        );"""

    with create_connection() as conn:
        if conn is not None:
            create_table(conn, sql_create_groups)
            create_table(conn, sql_create_subject_table)
            create_table(conn, sql_create_students_table)
            create_table(conn, sql_create_grades_table)
        else:
            print('Error: can\'t create the database connection')