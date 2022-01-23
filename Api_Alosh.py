import requests
from flask import Flask,request

app = Flask(__name__)
@app.route("/")

def index():
    return "<h1>Api Alosh : @aaalaaa </h1>"

@app.route('/User/instagram/Alosh/Tools/',methods=['GET'])
def Hhjjj():
    User = request.args.get("User")
    headers ={'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '1176',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
'origin': 'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
'x-asbd-id':'198387' ,
'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
'x-instagram-ajax': '72bda6b1d047',
'x-requested-with': 'XMLHttpRequest'} 
    url= "https://www.instagram.com/accounts/web_create_ajax/attempt/"
    data= {'email' : 'a@gmail.com',
'username': (f'{User}'),
'first_name': 'AA',
'opt_into_one_tap': 'false'}
    req = requests.post(url,headers=headers,data=data). text
    Uss =  ('{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}') 
    if Uss in req:
         return {"User":"True", "By_Telegram":"@aaalaaa")
    else:
        return {"User":"False", "By_Telegram":"@aaalaaa")
