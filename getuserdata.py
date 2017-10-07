import requests

# this code is used to get the user data
# the parameters required are the access_token (code), and the fields that you want to view from the user profile (to get more sensitive data, you need to acquire permissions from facebook)
# sample response - {"id":"10210335153482645","first_name":"Femi","gender":"male","email":"fbilesanmi\u0040gmail.com","picture":{"data":{"is_silhouette":false,"url":"https:\/\/fb-s-a-a.akamaihd.net\/h-ak-fbx\/v\/t1.0-1\/p50x50\/14720441_10207691262587025_2707455386688501511_n.jpg?oh=d1301998f75a1ba355d89c35654918b1&oe=5A15971D&__gda__=1515727757_6ca13ac1ebc438257290ffae3abaec23"}},"age_range":{"min":21}}

code = 'EAAFAu2zZC5TgBAGZBss82Tz9m3CbZCs3Ly3F1J3dfs8p7f1qAN6JzkOJpb7VWXe9qj9nOPUYjP4cLhgrE7FIHEVcO9AhP6ema74aW8z9SAyMvz9KaZBjFOxBKcBJejO8RttOkyxxHaQKpALIyiWcESCPQZCare9CUZBv5NTc1qOgZDZD'
fields = 'id,first_name,gender,email,picture,age_range,last_name,birthday,favorite_athletes,location,relationship_status,languages'
payload = {'access_token': code, 'fields': fields}
file = requests.post('https://graph.facebook.com/v2.7/me?', params=payload)

print(file.json())
print()
print(file.json()['first_name'])
