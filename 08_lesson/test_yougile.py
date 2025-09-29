import requests
import json

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
    result = api.get_id_company(login, password, name)
    id_company = result["content"][0]["id"]

    # 2. получить токен
    created_key = api.create_key(login, password, id_company)
    key_company = created_key["key"]

    # 3. создать проект
    created_project = api.create_project(key_company, title_project, users)
    id_project = created_project["id"]

    assert id_project is not None


def test_negative_create_project():
    # # 1. получить id компании
    # id_company = api.get_id_company(login, password, name)
    #
    # # 2. получить токен
    # key_company = api.create_key(login, password, id_company)

    # 3. создать проект
    key_company = ''
    id_project = api.create_project(key_company, title_project, users)

    assert id_project is None


def test_positive_change_title_project():
    # 1. получить id компании
    result = api.get_id_company(login, password, name)
    id_company = result["content"][0]["id"]

    # 2. получить токен
    created_key = api.create_key(login, password, id_company)
    key_company = created_key["key"]

    # 3. создать проект
    created_project = api.create_project(key_company, title_project, users)
    id_project = created_project["id"]

    # 4. изменить название проекта
    changed_project = api.change_title_project(
        key_company, new_title_project, users, id_project)
    id_changed_project = changed_project["id"]
    assert id_changed_project == id_project


def test_negative_change_title_project():
    # 1. получить id компании
    result = api.get_id_company(login, password, name)
    id_company = result["content"][0]["id"]

    # 2. получить токен
    created_key = api.create_key(login, password, id_company)
    key_company = created_key["key"]

    # # 3. создать проект
    # created_project = api.create_project(key_company, title_project, users)
    # id_project = created_project["id"]

    # 4. изменить название проекта
    id_project = ''
    id_changed_project = api.change_title_project(
         key_company, new_title_project, users, id_project)
    assert id_changed_project is None


def test_positive_get_title_project():
    # 1. получить id компании
    result = api.get_id_company(login, password, name)
    id_company = result["content"][0]["id"]

    # 2. получить токен
    created_key = api.create_key(login, password, id_company)
    key_company = created_key["key"]

    # 3. создать проект
    created_project = api.create_project(key_company, title_project, users)
    id_project = created_project["id"]

    # получить информацию о проекте
    get_title = api.get_title_project(key_company, id_project)
    get_title = get_title['title']
    assert get_title == title_project


def test_negative_get_title_project():
    # 1. получить id компании
    result = api.get_id_company(login, password, name)
    id_company = result["content"][0]["id"]

    # 2. получить токен
    created_key = api.create_key(login, password, id_company)
    key_company = created_key["key"]

    # # 3. создать проект
    # created_project = api.create_project(key_company, title_project, users)
    # id_project = created_project["id"]

    # получить информацию о проекте
    id_project = ''
    get_title = api.get_title_project(key_company, id_project)

    assert get_title is None
