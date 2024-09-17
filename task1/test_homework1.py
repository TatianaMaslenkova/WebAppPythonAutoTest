import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

S = requests.Session()


def test_create_post(user_login, get_description):
    res = S.post(url=data['post_address'], headers={'X-Auth-Token': user_login},
                 data={'title': data['title'], 'description': data['description'], 'content': data['content']}).status_code
    assert res == 200, 'create_post FAIL' # изменено
    # assert str(res) == '<Response [200]>', 'create_post FAIL'


def test_check_created_post(user_login, get_description):
    result = S.get(url=data['address'], headers={'X-Auth-Token': user_login}).json()['data']
    # print(result)
    description_list = [i['description'] for i in result]
    assert get_description in description_list, 'check_created_post FAIL'
