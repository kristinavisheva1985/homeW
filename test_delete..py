from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:15801163@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_db_connect():
    names = db.table_names()
    assert names[4] == 'teacher'


def test_db_insert():
    sql = text("""INSERT INTO teacher("teacher_id", "email", "group_id")
               VALUES (:teacher_id, :email, :group_id)""")

    with db.connect() as conn:
        # Вставка с параметрами
        conn.execute(sql,
                     teacher_id=33333,
                     email="kukukuku@mail.ru",
                     group_id=131)
        conn.execute("COMMIT")


def delete_teacher():
    with db.connect() as conn:
        conn.execute(text("""DELETE FROM teacher
                          WHERE "teacher_id" = 33333
                          AND "email" = 'kukukuku@mail.ru'"""))
        conn.execute("COMMIT")