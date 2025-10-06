from sqlalchemy import create_engine, text


class StudentTable:
    __scripts = {
        "insert_new": text("INSERT INTO student(\"user_id\","
                           " \"level\", \"education_form\","
                           " \"subject_id\") VALUES (:user_id, "
                           ":level, :education_form, :subject_id)"),
        "delete by id": text("DELETE FROM student "
                             "WHERE \"user_id\" = :user_id"),
        "select by id": text("SELECT * FROM student "
                             "WHERE \"user_id\" = :user_id"),
        "update by id": text("UPDATE student "
                             "SET \"education_form\" = :new_education_form "
                             "WHERE \"user_id\" = :user_id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create(self, user_id, level, education_form, subject_id):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["insert_new"], {
            "user_id": user_id,
            "level": level,
            "education_form": education_form,
            "subject_id": subject_id
        })
        conn.commit()
        conn.close()
        return result

    def delete(self, user_id):
        with self.__db.connect() as conn:
            conn.execute(self.__scripts["delete by id"], {"user_id": user_id})
            conn.commit()
            return {"detail": "Student successfully deleted"}

    def get_student_by_id(self, user_id):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts["select by id"], {"user_id": user_id}
        )
        student = result.mappings().all()
        conn.close()
        return student

    def change_education_form(self, user_id, new_education_form):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts["update by id"],
            {"new_education_form": new_education_form, "user_id": user_id})
        conn.commit()
        conn.close()
        return result
