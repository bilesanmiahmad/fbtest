import requests


def get_fb_token():
    app_id = 352648708482360
    app_secret = '5d949c0bc63b4d239b22b4abb968e1c7'
    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/v2.10/oauth/access_token?', params=payload)
    # print file.text #to test what the FB api responded with
    print(file.text)
    # result = file.text.split("=")[1]
    # print file.text #to test the TOKEN
    # return result
#     https://www.facebook.com/connect/login_success.html?code=AQBYQnpJ1B0fEjfTgwhJu3YRigyBaBtVFwnVRjb8LHjwNAJMO1_e6c2rYMaKghb4BEK4yJyhj3Oq16paA24TOD_1HN0XQUA_b9tfvbSt8mILBAuyf4EezAgK9obkZSsWQLd_sbMuegnGV6tpMOzhPHVBxle4PIpfEWu3PRI2oF2iS8qtw6HhJ7zFFkbB8W6duV9-Us9qMEE9_m7JCnqigfsvPyWx0DG1XUPswWUk1t-njVV9lSEhZYfZQOR6rmD8-wLmZhWbilmPBTKJu1qc770MWR_Tsg9-GeI7GBDWFmVW9gTvJjnK9zUvh92ZnpGx7dc#_=_
# https://www.facebook.com/connect/login_success.html?code=AQD4ZRKTkGubMv_GNuQ3VO_Z5vmELUwc36ECQ3rw1OAfdmxmH4IGPV-p1wA-ZYw2Gxz-8LqwlkOIU_w3b2DsyZHSMX7PUjffOfLsJiN8M_6Z3HWuf1xsW6RqAY3NpYY2pXZOd37PbGf-0Dnp5KyEz0y5ymaCUN44XLMbX1u26BI9HC5NHGA9dGCaZi7auRJ2nOcgs-jMkDgG7dldx_-ECOtEqcd3rx6AS3b8XyV3j5r7m-chHZAgC0NDJAYUuuFCXmPQuRNNIJsmWnKWSrMKd9jy-ZZM2PppHvaTKKGoOcTi58i1A7E0vhFskVdbMvtMXTA#_=_
# https://www.facebook.com/connect/login_success.html?code=AQDG4RB0Rjh6ychOCh_kJEkJUHgDA01mZ4AksTNam-CsySsHzYy8o_vZGbF7nfuvEkdYbjvrLyX2YBg6xjgdHyzLojAyi81FFzaYyA6WpufR-QDUzRCHFPGgCcADm27858n4fATyCg24tlYMdonHTbK2ldP_dTV6eev0uZ8uGhVPYFZfAZNSZQ5m8kvB8_VnyVYhg1I282SHL4nm-298ylkw9O8xwlKOlFW3xcShmsfNTUevAwwmbheSTUHZgkZr1oUJzSiw0Tjk5DEGbTnj5fQubDIMzr2ldiTpLxZk6qSfGf4a5saOYlCphTQQYBadUWI#_=_
get_fb_token()
