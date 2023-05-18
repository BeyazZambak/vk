import time
import requests
from pprint import pprint
token = ''

URL = 'https://api.vk.com/method/users.get'
params = {
    'user_ids': '1,2',
    'access_token': token,
    'v': '5.131',
    'fields': 'education,sex'
}
res = requests.get(URL, params)
pprint(res.json())

def search_groups(q, sorting=0):
    params = {
        'q': q,
        'access_token': token,
        'v': '5.131',
        'sort': sorting,
        'count': 300
        }
    req = requests.get('https://api.vk.com/method/groups.search', params).json()
    req = req['response']['items']
    return req

target_groups = search_groups('python')
pprint(target_groups)
