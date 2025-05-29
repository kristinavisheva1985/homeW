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
                     teacher_id=55556,
                     email="adsesrs@mail.ru",
                     group_id=222)

    sql = text("""SELECT * from teacher where teacher_id = (:teacher_id)""")
    with db.connect() as conn:
        # Вставка с параметрами
        result = conn.execute(sql,
                     teacher_id=55556)

    assert result.rowcount == 1



    with db.connect() as conn:
        conn.execute(text("""DELETE FROM teacher
                          WHERE "teacher_id" = 55556
                          """))
        conn.execute("COMMIT")

def test_db_update():
    sql = text("""INSERT INTO teacher("teacher_id", "email", "group_id")
               VALUES (:teacher_id, :email, :group_id)""")

    with db.connect() as conn:
        # Данные:
        conn.execute(sql,
                     teacher_id=66666,
                     email="lilili@mail.ru",
                     group_id=222)
        conn.execute("COMMIT")  # Фикс


    update_sql = text("""
        UPDATE teacher
        SET "email" = :new_email
        WHERE "teacher_id" = :teacher_id
        AND "email" = :old_email
    """)

    with db.connect() as conn:
        # Обновление email (lilili на kokoko)
        result = conn.execute(update_sql,
                              new_email="kokoko@mail.ru",
                              teacher_id=66666,
                              group_id=222,
                              old_email="lilili@mail.ru")
    sql = text("""SELECT * from teacher where teacher_id = (:teacher_id)""")
    with db.connect() as conn:
        # Вставка с параметрами
        result = conn.execute(sql,
                              teacher_id=66666).fetchall()

    assert result[0][1] == 'kokoko@mail.ru'


    with db.connect() as conn:
        conn.execute(text("""DELETE FROM teacher
                          WHERE "teacher_id" = 66666
                          AND "email" = 'kokoko@mail.ru'"""))
        conn.execute("COMMIT")


def test_delete_teacher():
    sql = text("""INSERT INTO teacher("teacher_id", "email", "group_id")
                   VALUES (:teacher_id, :email, :group_id)""")

    with db.connect() as conn:
        # Вставка с параметрами
        conn.execute(sql,
                     teacher_id=33333,
                     email="kukukuku@mail.ru",
                     group_id=131)
        conn.execute("COMMIT")
    sql = text("""SELECT * from teacher where teacher_id = (:teacher_id)""")
    with db.connect() as conn:
        # Вставка с параметрами
        result = conn.execute(sql,
                              teacher_id=33333)

    assert result.rowcount == 1

    with db.connect() as conn:
        conn.execute(text("""DELETE FROM teacher
                          WHERE "teacher_id" = 33333
                          AND "email" = 'kukukuku@mail.ru'"""))
        conn.execute("COMMIT")
    sql = text("""SELECT * from teacher where teacher_id = (:teacher_id)""")
    with db.connect() as conn:
        # Вставка с параметрами
        result = conn.execute(sql,
                              teacher_id=33333)

    assert result.rowcount == 0