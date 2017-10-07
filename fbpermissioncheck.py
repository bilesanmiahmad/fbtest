import requests
# 'https://graph.facebook.com/me/permissions?access_token=USER_ACCESS_TOKEN'
code = 'EAAFAu2zZC5TgBALY39qfF7YlZB9xp8BCE5uzFgBhptCiNQEv09LlhIFjWaoZC8WrvPpX905wPZAxzZC3kZCQScnEKPPo3LGbbc9gLXKq4dNIOKwMOuJgMXjJ9gdZBZBW9HO5SzE4g2rjv2mz4IIKMbgJzbMAPYhnGg1pOGDXjrxRzwZDZD'
permission_url = 'https://graph.facebook.com/me/permissions?access_token='+code
data = {'access_token': code}
permission_info = requests.get(permission_url)
redirect_url = 'https://com.projectcamy.fbsignin/oauth'
print(permission_info.json())
permission_data = permission_info.json()
print(permission_data['data'][0])
for data in permission_data['data']:
    if data['permission'] == 'user_friend':
        print(data['status'])
    else:
        print("Field does not exist")
