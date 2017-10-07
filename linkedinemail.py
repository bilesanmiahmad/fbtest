import requests

url = 'https://api.linkedin.com//v1/people/~/email-address?format=json'
access_token = 'Bearer AQV_Yj9cQXZASNicXgeOrwVSHT9mvL-Z_sC9cL_ODaT-yMowwjLHjHz8bJw1Hh-q0g3PwHmIY4TlnVPfVMNU4rJugx33-1o1jalHjwvmwDmfogBBgD9iRTYqzt_aPxv4zRZ7PWtAXpgkejmR-4J5zp7XmWpiv1hpmU2b3nsTuSaVKetvpuk'
headers = {'Authorization': access_token}
payload = {'oauth2_access_token': 'AQWqLZ3Ggstwuf-PmDcit9H4damNyq3QXMxzBAOE8ZsSxaFnKzDc-Emq1s3UQvGa7pbXRQAfqQgzfuA3kB6r7kQ3KSXufVafBXtnG-Tl9YofYQuXJ5Piy_HQ4Q9O3WZGm2AVio8loLxhyyAEW7s6743ZhYc5TAx_u4MiupOak8Tg957-5iA'}

user_data = requests.get(url, params=payload)
print(user_data.json())
