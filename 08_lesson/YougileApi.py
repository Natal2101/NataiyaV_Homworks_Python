import requests


class YougileApi:

    def __init__(self, url):
        self.url = url

    def get_id_company(self, login, password, name):
        params = {'limit': 50, 'offset': 0}
        headers = {'Content-Type': 'application/json'}
        data = {'login': login, 'password': password, 'name': name}
        resp = requests.post(f"{self.url}/api-v2/auth/companies",
                             params=params, headers=headers, json=data)
        return resp.json()

    def create_key(self, login, password, id_company):
        auth_data = {'login': login, 'password': password,
                     'companyId': id_company}
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(f"{self.url}/api-v2/auth/keys",
                             headers=headers, json=auth_data)
        return resp.json()

    def create_project(self, key_company, title_project, users):
        # 3. создать проект
        headers = {'Content-Type': 'application/json',
                   'Authorization': f"Bearer {key_company}"}
        body = {'title': title_project, 'users': users}
        resp = requests.post(f"{self.url}/api-v2/projects",
                             headers=headers, json=body)
        return resp.json()

    def change_title_project(self, key_company, new_title_project,
                             users, id_project):
        headers = {'Content-Type': 'application/json',
                   'Authorization': f"Bearer {key_company}"}
        data_for_change_title = {'deleted': True, 'title': new_title_project,
                                 'users': users}
        resp = requests.put(f"{self.url}/api-v2/projects/{id_project}",
                            headers=headers, json=data_for_change_title)
        return resp.json()

    def get_title_project(self, key_company, id_project):
        headers = {'Content-Type': 'application/json',
                   'Authorization': f"Bearer {key_company}"}
        resp = requests.get(f"{self.url}/api-v2/projects/{id_project}",
                            headers=headers)
        return resp.json()
