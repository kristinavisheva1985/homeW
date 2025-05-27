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
        # Данные:
        conn.execute(sql,
                     teacher_id=66666,
                     email="lilili@mail.ru",
                     group_id=222)
        conn.execute("COMMIT")  # Фикс


def update_teacher_email():
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
        assert result[0] == "kokoko@mail.ru"


def delete_teacher():
    with db.connect() as conn:
        conn.execute(text("""DELETE FROM teacher
                          WHERE "teacher_id" = 66666
                          AND "email" = 'kokoko@mail.ru'"""))
        conn.execute("COMMIT")