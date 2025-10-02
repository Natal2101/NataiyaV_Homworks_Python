from YougileApi import YougileApi

api = YougileApi("https://ru.yougile.com")
login = ''
password = ''
id_company = ''
title_project = 'Title Project'
new_title_project = 'New Title Project'
users = {}


def test_positive_create_project():
    try:
        # 1. получить токен
        key_company_response = api.create_key(login, password, id_company)

        if key_company_response.status_code != 201:
            print(f"Ошибка получения токена: "
                  f"{key_company_response.status_code} - "
                  f"{key_company_response.text}")
            return False

        assert key_company_response.status_code == 201

        key_company = key_company_response.json()["key"]
        print(f"Токен успешно получен: {key_company[:10]}...")

        # 2. создать проект
        create_project_response = api.create_project(
            key_company, title_project, users)

        if create_project_response.status_code != 201:
            print(f"Ошибка создания проекта: "
                  f"{create_project_response.status_code} - "
                  f"{create_project_response.text}")
            return False

        assert create_project_response.status_code == 201

        id_project = create_project_response.json()["id"]
        print(f"Проект успешно создан с ID: {id_project}")

        assert id_project
        assert len(id_project) > 0

        print("Тест test_positive_create_project пройден успешно!")
        return True

    except Exception as e:
        print(f"Произошла ошибка в test_positive_create_project: {str(e)}")
        return False


def test_negative_create_project():
    try:
        key_company = 'none-key-company'
        create_project_response = api.create_project(
            key_company, title_project, users)

        if create_project_response.status_code != 401:
            print(f"Ожидался статус 401, но получен "
                  f"{create_project_response.status_code}")
            return False

        assert create_project_response.status_code == 401

        response_json = create_project_response.json()
        error_message = response_json.get('error', 'Неизвестная ошибка')
        print(f"Проект не был создан. "
              f"Произошла ошибка авторизации: {error_message}")

        # Проверяем наличие поля "error"
        assert 'error' in response_json
        assert 'id' not in response_json  # в ошибке не должно быть ID проекта

        print("Тест test_negative_create_project пройден успешно!")
        return True

    except Exception as e:
        print(f"Произошла ошибка в test_negative_create_project: {str(e)}")
        return False


def test_positive_change_title_project():
    try:
        key_company_response = api.create_key(login, password, id_company)

        if key_company_response.status_code != 201:
            print(
                f"Ошибка получения токена: {key_company_response.status_code}")
            return False

        assert key_company_response.status_code == 201

        key_company = key_company_response.json()["key"]
        print(f"Токен успешно получен: {key_company[:10]}...")

        create_project_response = api.create_project(
            key_company, title_project, users)

        if create_project_response.status_code != 201:
            print(
                f"Ошибка создания проекта: "
                f"{create_project_response.status_code}")
            return False

        assert create_project_response.status_code == 201

        id_project = create_project_response.json()["id"]
        print(f"Проект успешно создан с ID: {id_project}")

        # 2. изменить название проекта
        change_title_response = api.change_title_project(
            key_company, new_title_project, users, id_project)

        if change_title_response.status_code != 200:
            print(
                f"Ошибка изменения названия проекта:"
                f" {change_title_response.status_code} -"
                f" {change_title_response.text}")
            return False

        assert change_title_response.status_code == 200

        status_code = change_title_response.status_code
        print(f"Проект успешно изменен. Статус-код:{status_code}")

        response_json = change_title_response.json()
        assert 'id' in response_json

        id_changed_project = change_title_response.json()["id"]
        assert id_changed_project == id_project

        print("Тест test_positive_change_title_project пройден успешно!")
        return True

    except Exception as e:
        print(
            f"Произошла ошибка в test_positive_change_title_project: {str(e)}")
        return False


def test_negative_change_title_project():
    try:
        key_company_response = api.create_key(login, password, id_company)

        if key_company_response.status_code != 201:
            print(f"Ошибка получения токена: "
                  f"{key_company_response.status_code}")
            return False

        assert key_company_response.status_code == 201

        key_company = key_company_response.json()["key"]
        print(f"Токен успешно получен: {key_company[:10]}...")

        # изменить название проекта
        id_project = 'none-project-id'
        change_title_response = api.change_title_project(
            key_company, new_title_project, users, id_project)

        if change_title_response.status_code != 404:
            print(f"Ожидался статус 404, "
                  f"но получен {change_title_response.status_code}")
            return False

        assert change_title_response.status_code == 404

        status_code = change_title_response.status_code
        response_json = change_title_response.json()
        error_message = response_json.get('error', 'Неизвестная ошибка')
        print(f"Проект не был изменен. Статус-код:{status_code}. "
              f"Произошла ошибка: {error_message}")

        assert 'error' in response_json
        assert 'id' not in response_json  # в ошибке не должно быть ID

        print("Тест test_negative_change_title_project пройден успешно!")
        return True

    except Exception as e:
        print(
            f"Произошла ошибка в test_negative_change_title_project: {str(e)}")
        return False


def test_positive_get_title_project():
    try:
        key_company_response = api.create_key(login, password, id_company)

        if key_company_response.status_code != 201:
            print(f"Ошибка получения токена: "
                  f"{key_company_response.status_code}")
            return False

        assert key_company_response.status_code == 201

        key_company = key_company_response.json()["key"]
        print(f"Токен успешно получен: {key_company[:10]}...")

        create_project_response = api.create_project(
            key_company, title_project, users)

        if create_project_response.status_code != 201:
            print(f"Ошибка создания проекта: "
                  f"{create_project_response.status_code}")
            return False

        assert create_project_response.status_code == 201

        id_project = create_project_response.json()["id"]
        print(f"Проект успешно создан с ID: {id_project}")

        # 2. получить информацию о проекте
        get_title_response = api.get_title_project(key_company, id_project)

        if get_title_response.status_code != 200:
            print(f"Ошибка получения проекта: "
                  f"{get_title_response.status_code} -"
                  f" {get_title_response.text}")
            return False

        assert get_title_response.status_code == 200

        status_code = get_title_response.status_code
        print(f"Информация о проекте успешно получена. "
              f"Статус-код:{status_code}")

        get_title = get_title_response.json()['title']
        assert get_title == title_project

        # Дополнительные проверки
        response_json = get_title_response.json()
        assert 'id' in response_json
        assert 'users' in response_json

        print("Тест test_positive_get_title_project пройден успешно!")
        return True

    except Exception as e:
        print(f"Произошла ошибка в test_positive_get_title_project: {str(e)}")
        return False


def test_negative_get_title_project():
    try:
        key_company_response = api.create_key(login, password, id_company)

        if key_company_response.status_code != 201:
            print(f"Ошибка получения токена: "
                  f"{key_company_response.status_code}")
            return False

        assert key_company_response.status_code == 201

        key_company = key_company_response.json()["key"]
        print(f"Токен успешно получен: {key_company[:10]}...")

        # получить информацию о проекте
        id_project = 'none-project-id'
        get_title_response = api.get_title_project(key_company, id_project)

        if get_title_response.status_code != 404:
            print(f"Ожидался статус 404, но получен "
                  f"{get_title_response.status_code}")
            return False

        assert get_title_response.status_code == 404
        status_code = get_title_response.status_code
        response_json = get_title_response.json()
        error_message = response_json.get('error', 'Неизвестная ошибка')
        print(f"Информация о проекте не была получена. "
              f"Статус-код:{status_code}. "
              f"Произошла ошибка: {error_message}")

        assert 'error' in response_json
        assert 'title' not in response_json  # в ошибке не должно быть
        # названия проекта

        print("Тест test_negative_get_title_project пройден успешно!")
        return True

    except Exception as e:
        print(f"Произошла ошибка в test_negative_get_title_project: {str(e)}")
        return False
