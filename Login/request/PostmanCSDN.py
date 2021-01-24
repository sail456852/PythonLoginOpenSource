import requests

#not succeed due to limitation
url = "https://passport.csdn.net/v1/register/pc/login/doLogin"

payload = "{\"loginType\":\"1\",\"pwdOrVerifyCode\":\"sss\",\"userIdentification\":\"yourEmail\"}"
headers = {
    'authority': 'passport.csdn.net',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'accept': 'application/json, text/plain, */*',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'x-tingyun-id': 'im-pGljNfnc;r=514063905',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://passport.csdn.net',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://passport.csdn.net/login?code=public',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'cookie': 'uuid_tt_dd=10_20282818330-1600869425948-729755; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%7D; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_20282818330-1600869425948-729755; __gads=ID=630ac09a7cfc562f:T=1602155119:S=ALNI_MaWyB6gYElH5X9TFXuIpArn3tu4jQ; _ga=GA1.2.646731675.1602993485; c-login-auto=1; c_first_ref=default; c_first_page=https%3A//www.csdn.net/c/jlnzjqw0; c_segment=11; is_advert=1; dc_sid=6307b3687f527d9d8ea387e2e7f8bb81; log_Id_view=225; log_Id_click=3; TY_SESSION_ID=6cac79f3-2951-4dca-ac01-589d08719126; c_pref=; c_ref=https%3A//github.com/; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1609677888,1609679198,1610507679,1610507696; dc_session_id=10_1610514047781.379648; c_page_id=default; SESSION=93a9b7fd-dca1-47fa-99de-d733a5f20301; announcement-new=%7B%22isLogin%22%3Afalse%2C%22announcementUrl%22%3A%22https%3A%2F%2Fblog.csdn.net%2Fblogdevteam%2Farticle%2Fdetails%2F112280974%3Futm_source%3Dgonggao_0107%22%2C%22announcementCount%22%3A0%7D; dc_tos=qmuwlh; log_Id_pv=76; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1610514054; SESSION=35e5317a-78b3-4ef0-b9ef-f0849e3b7b41'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
