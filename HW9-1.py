from pprint import pprint
import requests

url = "https://superheroapi.com/api/2619421814940190/search/"
list = ['Hulk', 'Captain America', 'Thanos']

def superhero(list, url):
    url_list = []
    result_dict = {}
    for name in list:
        assert isinstance(name, object)
        url_list.append(url + name)

    for i in url_list:
        response = requests.get(i, timeout=5)
        # pprint(response.json())
        names = response.json()['results'][0]['name']
        result_dict[names] = int(response.json()['results'][0]['powerstats']['intelligence'])
    pprint(f'общие результаты {result_dict}')
    pprint(f'победил {max(result_dict.items())}')

superhero(list, url)


