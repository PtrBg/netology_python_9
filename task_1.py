import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url).json()
filtered_heroes = {}
for hero in resp:
	if hero['name'] in ('Hulk', 'Captain America', 'Thanos'):
		filtered_heroes[hero['name']] = hero['powerstats']['intelligence']
print(f'{max(filtered_heroes, key = lambda x: filtered_heroes[x])} самый умный')
