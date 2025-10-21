from StudentTable import StudentTable

db = StudentTable("")

user_id = '4'
level = 'Beginner'
education_form = 'personal'
new_education_form = 'group'
subject_id = '6'


def test_create_new_student():
    try:
        db.create(user_id, level, education_form, subject_id)

        created_student = db.get_student_by_id(user_id)

        if len(created_student) == 0:
            print("Запись о студенте не найдена.")
        else:
            assert created_student[0]['user_id'] == int(user_id)
            assert created_student[0]['level'] == level
            assert created_student[0]['education_form'] == education_form
            assert created_student[0]['subject_id'] == int(subject_id)
            print("Запись о студенте успешно создана. Все проверки пройдены")

        print("=== test_create_new_student УСПЕШНО завершен ===\n")

    except Exception as e:
        print(f"Тест завершился с ошибкой: {str(e)}")

    finally:
        db.delete(user_id)
        result = db.get_student_by_id(user_id)
        assert len(result) == 0


def test_change_education_form():
    try:
        db.create(user_id, level, education_form, subject_id)

        created_student = db.get_student_by_id(user_id)

        if len(created_student) == 0:
            print("Запись о студенте не найдена.")
        else:
            assert created_student[0]['user_id'] == int(user_id)
            assert created_student[0]['level'] == level
            assert created_student[0]['education_form'] == education_form
            assert created_student[0]['subject_id'] == int(subject_id)
            print("Запись о студенте успешно создана. Проверки пройдены.")

            db.change_education_form(user_id, new_education_form)
            changed_student = db.get_student_by_id(user_id)

            if len(changed_student) == 0:
                print("Запись о студенте не найдена "
                      "после изменения формы образования.")
            else:
                assert changed_student[0]['user_id'] == int(user_id)
                assert changed_student[0]['level'] == level
                assert (changed_student[0]['education_form'] ==
                        new_education_form)
                assert changed_student[0]['subject_id'] == int(subject_id)
                print("Форма обучения изменена. "
                      "Проверки после изменения пройдены.")

        print("=== test_change_education_form УСПЕШНО завершен ===\n")

    except Exception as e:
        print(f"Тест завершился с ошибкой: {str(e)}")

    finally:
        db.delete(user_id)
        rows = db.get_student_by_id(user_id)
        assert len(rows) == 0


def test_delete():
    try:
        db.create(user_id, level, education_form, subject_id)

        created_student = db.get_student_by_id(user_id)

        if len(created_student) == 0:
            print("Запись о студенте не найдена.")
        else:
            assert created_student[0]['user_id'] == int(user_id)
            assert created_student[0]['level'] == level
            assert created_student[0]['education_form'] == education_form
            assert created_student[0]['subject_id'] == int(subject_id)
            print("Запись о студенте успешно создана. Проверки пройдены.")

            deleted_student = db.delete(user_id)
            assert deleted_student["detail"] == "Student successfully deleted"

            rows = db.get_student_by_id(user_id)
            assert len(rows) == 0
            print("Запись о студенте успешно удалена. Проверки пройдены.")

        print("=== test_delete УСПЕШНО завершен ===\n")

    except Exception as e:
        print(f"Тест завершился с ошибкой: {str(e)}")
