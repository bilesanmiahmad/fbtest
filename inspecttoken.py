import requests

# This is used to get details about the access token, which includes info like expiration date, application using the code/token, scope of the token.
# the parameters used are the input token which is the access token generated for a user from (accesstokentest.py), the access token is the access token for the app
# {"data":{"app_id":"352648708482360","type":"USER","application":"Camy","expires_at":1509814300,"is_valid":true,"issued_at":1504630300,"scopes":["email","public_profile"],"user_id":"10210335153482645"}}

app_id = 352648708482360
app_secret = '5d949c0bc63b4d239b22b4abb968e1c7'
redirect_uri = 'https://www.facebook.com/connect/login_success.html'
code = 'AQC4JFvN4_TP-D2ofKi0bN2oEsboiW6Lvi7SlW8orHZLjsaQPsiw8NYAhlTHx2QHPNuKkJf0Z954pAj2VQP13BcoHkWSmm0HLM3rBDNgh6bbdK9w8OU8Os3CEC4Vklw1iZqRnRtVPHvjWoj3bYiNzIKljUNo_MBz3V68xiNirlzcLzF0QZZlMGSDBqgOsf7fL9rxF8gBrQngTnFez6baS9PVjHsVj-sQr5mf-oDioSH__onRc50nSgARVacye82EbfJ6bTr0nrjcioulGXJLZhL5EFLgIco1qYyquhF93CLoSq6dAYq6JxJ3OHHsKZ6NM5k#_=_'

# input_tok = 'EAAFAu2zZC5TgBAOns31ZC6y0DUarcrZAHF5JBUsHgzD0tHpZCQLc47FtiXIjl3ix3oBBOuo42GuZA0bw8SbwmZBxM1y0lZAinSvkAoVDhVgS9aUGITw9psbSNztL36HsTPJEKom5qD0cwoEDVOjiuyvlVLJEwWkYZCfunI2f2QsWbwZDZD'
# access_tok = '352648708482360|Nejr2RanF2M9vykeM-LqKBD88v8'
# payload = {'input_token': input_tok, 'access_token': access_tok}
# file = requests.get('https://graph.facebook.com/debug_token?', params=payload)
file_json = file.json()
print(file_json)
print(file_json['data']['expires_at'])
# print(file.text)
