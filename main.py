import requests


def get_intel(name_list):
  hero_dict = {}
  for name in name_list:
    response_id = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{name}')
    res = response_id.json()
    id = res['results'][0]['id']
    response_int = requests.get(f'https://superheroapi.com/api/2619421814940190/{id}/powerstats')
    int = response_int.json()
    hero_dict.update({name:int['intelligence']})
  a = list(hero_dict.items())
  a.sort(key=lambda p: p[1])
  print(a[0][0])


if __name__ == '__main__':
  get_intel(['Hulk', 'Captain America', 'Thanos',])
