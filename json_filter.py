import json

file = open('data.json')
data = json.load(file)
for emp in data['data']:
    if emp['id'] == 34:
        print(emp)
print(data['data'])
