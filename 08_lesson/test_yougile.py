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
    id_company = api.get_id_company(login, password, name)["content"][0]["id"]
    # 2. получить токен
    key_company = api.create_key(login, password, id_company)["key"]
    # 3. создать проект
    created_project = api.create_project(key_company, title_project, users)
    id_project = created_project["id"]

    assert id_project is not None


def test_negative_create_project():
    key_company = 'none-key-company'
    response = api.create_project(key_company, title_project, users)

    assert response.get('error')  # проверяем наличие поля "error"
    assert isinstance(response.get('error'), str)


def test_positive_change_title_project():
    # 1. создать проект
    id_company = api.get_id_company(login, password, name)["content"][0]["id"]
    key_company = api.create_key(login, password, id_company)["key"]
    id_project = api.create_project(key_company, title_project, users)["id"]

    # 2. изменить название проекта
    id_changed_project = api.change_title_project(
        key_company, new_title_project, users, id_project)["id"]

    assert id_changed_project == id_project


def test_negative_change_title_project():
    id_company = api.get_id_company(login, password, name)["content"][0]["id"]
    key_company = api.create_key(login, password, id_company)["key"]

    # изменить название проекта
    id_project = 'none-project-id'
    response = api.change_title_project(
         key_company, new_title_project, users, id_project)

    assert response.get('error')  # проверка наличия поля ошибки
    assert isinstance(response.get('error'), str)


def test_positive_get_title_project():
    # 1. создать проект
    id_company = api.get_id_company(login, password, name)["content"][0]["id"]
    key_company = api.create_key(login, password, id_company)["key"]
    id_project = api.create_project(key_company, title_project, users)["id"]

    # 2. получить информацию о проекте
    get_title = api.get_title_project(key_company, id_project)['title']

    assert get_title == title_project


def test_negative_get_title_project():
    id_company = api.get_id_company(login, password, name)["content"][0]["id"]
    key_company = api.create_key(login, password, id_company)["key"]

    # получить информацию о проекте
    id_project = 'none-project-id'
    response = api.get_title_project(key_company, id_project)

    assert response.get('error')  # проверка наличия поля ошибки
    assert isinstance(response.get('error'), str)
