from YougileApi import YougileApi


api = YougileApi("https://ru.yougile.com")
login = ''
password = ''
name = ''
title_project = 'Title Project'
new_title_project = 'New Title Project'
users = {}


def test_create_project():
    # 1. получить id компании
    id_company = api.get_id_company(login, password, name)

    # 2. получить токен
    key_company = api.create_key(login, password, id_company)

    # 3. создать проект
    id_project = api.create_project(key_company, title_project, users)
    assert id_project is not None


def test_change_title_project():
    # 1. получить id компании
    id_company = api.get_id_company(login, password, name)

    # 2. получить токен
    key_company = api.create_key(login, password, id_company)

    # 3. создать проект
    id_project = api.create_project(key_company, title_project, users)

    # 4. изменить название проекта
    id_changed_project = api.change_title_project(
        key_company, new_title_project, users, id_project)
    assert id_changed_project == id_project


def test_get_title_project():
    # 1. получить id компании
    id_company = api.get_id_company(login, password, name)

    # 2. получить токен
    key_company = api.create_key(login, password, id_company)

    # 3. создать проект
    id_project = api.create_project(key_company, title_project, users)

    # получить информацию о проекте
    get_title = api.get_title_project(key_company, id_project)

    assert get_title == title_project
