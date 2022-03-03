import requests

people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()

print(json)

print('The People currently in space are:')
for person in json['people']:
    print(person['name'])