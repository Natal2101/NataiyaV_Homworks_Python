from http.client import responses


from YougileApi import YougileApi


api = YougileApi("https://ru.yougile.com")
login = ''
password = ''
name = ''
title_project = 'Title Project'
new_title_project = 'New Title Project'
users = {}


def test_positive_create_project():
    # 1. получить id компании
    id_company = api.get_id_company(
        login, password, name)["content"][0]["id"]
    # 2. получить токен
    key_company = api.create_key(login, password, id_company)["key"]
    # 3. создать проект
    response_json, status_code = api.create_project(
        key_company, title_project, users)
    id_project = response_json["id"]
    assert status_code == 201
    assert id_project is not None


def test_negative_create_project():
    key_company = 'none-key-company'
    response_json, status_code = api.create_project(
        key_company, title_project, users)
    assert status_code == 401
    assert response_json.get('error')  # проверяем наличие поля "error"
    assert isinstance(response_json.get('error'), str)


def test_positive_change_title_project():
    # 1. создать проект
    response = api.get_id_company(login, password, name)
    id_company = response["content"][0]["id"]
    key_company = api.create_key(login, password, id_company)["key"]
    result = api.create_project(key_company, title_project, users)
    response_json, status_code = result
    id_project = response_json["id"]

    # 2. изменить название проекта
    response_json, status_code = api.change_title_project(
        key_company, new_title_project, users, id_project)
    id_changed_project = response_json["id"]
    assert status_code == 200
    assert id_changed_project == id_project


def test_negative_change_title_project():
    response = api.get_id_company(login, password, name)
    id_company = response["content"][0]["id"]
    key_company = api.create_key(login, password, id_company)["key"]

    # изменить название проекта
    id_project = 'none-project-id'
    response_json, status_code = api.change_title_project(
         key_company, new_title_project, users, id_project)
    assert status_code == 404
    assert response_json.get('error')  # проверка наличия поля ошибки
    assert isinstance(response_json.get('error'), str)


def test_positive_get_title_project():
    # 1. создать проект
    response = api.get_id_company(login, password, name)
    id_company = response["content"][0]["id"]
    key_company = api.create_key(login, password, id_company)["key"]
    result = api.create_project(key_company, title_project, users)
    response_json, status_code = result
    id_project = response_json["id"]

    # 2. получить информацию о проекте
    response_json, status_code = api.get_title_project(key_company, id_project)
    get_title = response_json['title']
    assert status_code == 200
    assert get_title == title_project


def test_negative_get_title_project():
    response = api.get_id_company(login, password, name)
    id_company = response["content"][0]["id"]
    result = api.create_key(login, password, id_company)
    key_company = result["key"]

    # получить информацию о проекте
    id_project = 'none-project-id'
    response_json, status_code = api.get_title_project(key_company, id_project)
    assert status_code == 404
    assert response_json.get('error')  # проверка наличия поля ошибки
    assert isinstance(response_json.get('error'), str)
