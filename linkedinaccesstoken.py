import requests
import datetime
import json

grant_type = 'authorization_code'
app_id = '777lpxpde1v7ao'
app_secret = '0gIX9sxCQVZJvbzD'
redirect_uri = 'https://www.flaregh.com/'
code = 'AQTqfNFOAO1CwIGEAkpq4B7VHpSdUstn-4LIe1_-5TVGRI-uRs-nurH0KJY9BOCtorYhDZy88uqwsFoYR0Lil7d9dz5rf37j_952AnyBL1Cya3KkWP5j5cLfM87d1vcsx7Kx4R8GzD1RRLNKByvbUk6b7GsL3Q'
payload = {'grant_type': grant_type, 'client_id': app_id, 'redirect_uri': redirect_uri, 'client_secret': app_secret, 'code': code}
file = requests.get('https://www.linkedin.com/oauth/v2/accessToken', params=payload)

print(file.text)
expires_in = file.json()['expires_in']
expires_in_seconds = datetime.timedelta(seconds=expires_in)
print(expires_in_seconds)

# https://www.flaregh.com/?code=AQSSVPogykO7uZ39rFQsKHfIy9W6JjKxy3puFaNs6Pg9-By--MkZviJUJs280vmpZ0l8jefk5naHhs8Oz7YBfrBKUXVTycHKotQh0JqdFI1pSDaxw4NYnB-9yDRIrL2-9mYWy7LeWPao-E0gvsfjcw84AIsRwQ&state=987654321r_fullprofile+r_emailaddress
