import requests
import time

grant_type = 'authorization_code'
app_id = '777lpxpde1v7ao'
app_secret = '0gIX9sxCQVZJvbzD'
redirect_uri = 'https://www.flaregh.com/'
code = 'AQQfhyoUfF4Jei4OCd6K3XYOWMISvCJmFvXECMLv1qLdfDWGjK4kyJNYRN5bVW3ajvHp73CNThkkvJ1v2_gfvetdwPqP78XfPaeerTOFiRjy72zXxRLY2RiEKZulUJet33RJt1Cg1QY8Qs7_OAs94oE_S9kM4A'
access_payload = {'grant_type': grant_type, 'client_id': app_id, 'redirect_uri': redirect_uri, 'client_secret': app_secret, 'code': code}
file = requests.get('https://www.linkedin.com/oauth/v2/accessToken', params=access_payload)
token_data_json = file.json()
print(token_data_json)
token = token_data_json['access_token']
# token = 'AQU3-noLgjQPJenXWWP6VJlIuzqL9OdqD6xDd2yLq_D7JmV0b0jP0JPEiUbJdhSoIGQh3H2lt_tYamEtuw84-1rVIvoFJRoYn4nil2NX4S_Q9BQIRtFIeY0Aor5I1E6bJODTA4Py_N9gbqVOWSCrvzQi_NWcanfn_p9FXvqQ_0ypYi1zSa0'
print(token)
# time.sleep(25)

url = 'https://api.linkedin.com/v1/people/~?format=json'

# payload = {'oauth2_access_token': token}
headers = {'Authorization': 'Bearer ' + token}

user_data = requests.get(url, headers=headers)
# user_data = requests.get(url, params=payload)
print(user_data.json())

email_url = 'https://api.linkedin.com/v1/people/~/email-address?format=json'

email_payload = {'oauth2_access_token': token}

email_user_data = requests.get(email_url, params=email_payload)
print(email_user_data.json())

########################################################################

# time.sleep(15)

url = 'https://api.linkedin.com/v1/people/~?format=json'

# payload = {'oauth2_access_token': token}
headers = {'Authorization': 'Bearer ' + token}

user_data = requests.get(url, headers=headers)
# user_data = requests.get(url, params=payload)
print(user_data.json())

email_url = 'https://api.linkedin.com//v1/people/~/email-address?format=json'

email_payload = {'oauth2_access_token': token}

email_user_data = requests.get(email_url, params=email_payload)
print(email_user_data.json())

###########################################################################

# time.sleep(15)

url = 'https://api.linkedin.com//v1/people/~?format=json'

# payload = {'oauth2_access_token': token}
headers = {'Authorization': 'Bearer ' + token}

user_data = requests.get(url, headers=headers)
# user_data = requests.get(url, params=payload)
print(user_data.json())

email_url = 'https://api.linkedin.com//v1/people/~/email-address?format=json'

email_payload = {'oauth2_access_token': token}

email_user_data = requests.get(email_url, params=email_payload)
print(email_user_data.json())
