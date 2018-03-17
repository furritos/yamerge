from time import sleep

import requests
from furl import furl

BASE_URL = furl('https://www.yammer.com/')


def url_builder(uri, parameters=None):
    BASE_URL.path.segments = uri
    if parameters:
        BASE_URL.add(parameters)
    else:
        BASE_URL.args = {}
    return BASE_URL.url


def get_group_url(gid, parameters=None):
    uri = ['api', 'v1', 'users', 'in_group', gid]
    return url_builder(uri, parameters)


def post_group_url(parameters=None):
    uri = ['api', 'v1', 'group_memberships.json']
    return url_builder(uri, parameters)


def get_auth_session(token):
    auth_session = requests.Session()
    auth_session.headers.update({'Authorization': 'Bearer {}'.format(token)})
    return auth_session


def get_user_ids_in_group(session, gid):
    page_counter = 0
    definitive_user_list = []
    print('Finding users for group ID {}'.format(gid))
    while True:
        page_counter += 1
        result = session.get(url=get_group_url(gid=gid, parameters={'page': page_counter}))
        users_list = result.json().get('users')
        for user in users_list:
            definitive_user_list.append(user.get('id'))
        if len(users_list) != 50:
            print('Found {} users, reached the last page and breaking...\n\r'.format(len(users_list)))
            break
        print('Found {} users in page {}, sleeping for a bit...'.format(len(users_list), page_counter))
        sleep(2)
    return definitive_user_list


def add_users_to_group(session, payload, gid):
    for uid in payload:
        print('ID to be added: {}'.format(uid))
        user_to_group_entity = {'group_id': gid, 'user_id': uid}
        result = session.post(url=post_group_url(), json=user_to_group_entity)
        if result.status_code != 201:
            print('ID was not successfully processed, status code: [{}]'.format(result.status_code))
        sleep(2)


def from_sweet_potatoes_to_yams(dt, mgid, sgid):
    user_session = get_auth_session(dt)
    master_group_list = get_user_ids_in_group(user_session, mgid)
    slave_group_list = get_user_ids_in_group(user_session, sgid)
    delta_list = list(set(master_group_list) - set(slave_group_list))
    add_users_to_group(user_session, delta_list, sgid)
