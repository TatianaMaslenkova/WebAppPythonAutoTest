import logging
import requests
import yaml

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

session = requests.Session()


def test_create_post(get_token):
    res = session.post(url=testdata['post_address'], headers={'X-Auth-Token': get_token},
                       data={'title': testdata['title'], 'description': testdata['description'],
                             'content': testdata['content']}).status_code
    logging.debug(f"Response code: {res}")
    assert res == 200, 'create_post FAIL'


def test_check_created_post(get_token):
    result = session.get(url=testdata['api_address'], headers={'X-Auth-Token': get_token}).json()['data']
    logging.debug(f"Get request return: {result}")
    list_description = [i['description'] for i in result]
    assert testdata['description'] in list_description, 'check_created_post FAIL'
