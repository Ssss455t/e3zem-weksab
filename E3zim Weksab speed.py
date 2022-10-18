import requests as rq,json,random
from bs4 import BeautifulSoup as BS 
import threading
import requests 
def all():
	
	number ='01559166187' #input("》 Enter Your Number : ")
	password ='sMz@Gz8mmZv6kGu' #input("》Enter Your Password : ")
	
	with rq.Session() as req:
	    
	    letters = 'qwertyuioplkjhgfdsazxcvbnm'
	    rand=''.join(random.choice(letters) for i in range(10))
	        
	    Url= f'https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/auth?client_id=website&redirect_uri=https%3A%2F%2Fweb.vodafone.com.eg%2Far%2FKClogin&state=286d1217-db14-4846-86c1-9539beea01ed&response_mode=query&response_type=code&scope=openid&nonce={rand}&kc_locale=en'
	    
	    R= req.get(Url)
	       
	    soup=BS (R.content,'html.parser')
	    URL=soup.find('form').get ('action')
	
	    HEADERS= {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'Accept-Encoding': 'gzip, deflate, br',
	    'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Host': 'web.vodafone.com.eg',
	    'Origin': 'https://web.vodafone.com.eg',
	    'Referer': Url,
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
	    }
	    
	    DATA= {
	    'username':number,
	    'password':password
	    }
	    
	    send_data =req.post(URL,headers=HEADERS, data=DATA).url   
	    code = (send_data[138:])
	    
	    
	    
	    URL1='https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token'
	
	    HEADERS1= {
	        'Accept': '*/*',
	        'Accept-Encoding': 'gzip, deflate, br',
	        'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
	        'Connection': 'keep-alive',
	        'Content-type': 'application/x-www-form-urlencoded',
	        'Host': 'web.vodafone.com.eg',
	        'Origin': 'https://web.vodafone.com.eg',
	        'Referer': 'https://web.vodafone.com.eg/ar/KClogin',
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
	        }  
	    DATA1= {
	        'code': code,
	        'grant_type': 'authorization_code',
	        'client_id': 'website',
	        'redirect_uri': 'https://web.vodafone.com.eg/ar/KClogin'
	        }  
	    token_request= req.post(URL1,headers=HEADERS1,data=DATA1)
	    access_token = token_request.json()['access_token']
	    
	    
	url0='https://web.vodafone.com.eg/services/dxl/promo/promotion'
		
	headers0 ={
		'Host': 'web.vodafone.com.eg',
		'Connection': 'keep-alive',
		'Content-Length': '145',
		'sec-ch-ua': '{"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"}',
		'DNT': '1',
		'msisdn': f'{number}',
		'Accept-Language': 'AR',
		'sec-ch-ua-mobile': '?1',
		'Authorization': f'Bearer {access_token}',
		'Content-Type': 'application/json',
		'Accept': 'application/json',
		'clientId': 'WebsiteConsumer',
		'xdtpc':'17$67079555_399h12vKGKQGUVVRESTGIALPOFORICHAEFKASLU-0e0',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
		
		'channel': 'WEB',
		'Origin': 'https://web.vodafone.com.eg',
		'Sec-Fetch-Site': 'same-origin',
		'Sec-Fetch-Mode': 'cors',
		
		'Sec-Fetch-Dest': 'empty',
		
		'Referer': 'https://web.vodafone.com.eg/spa/portal/mgm',
		'Accept-Encoding': 'gzip, deflate, br'
		}
		
	while True :
			
		int='1234567890'
		rr=''.join (random.choice (int)for i in range (8))
		invited_number=f"010{rr}"
			
			
		data0={
			  "@type": "Promo",
			  "channel": {
			    "id": "5"
			  },
			  "context": {
			    "type": "MGMInvite"
			  },
			  "pattern": [
			    {
			      "characteristics": [
			        {
			          "name": "AMsisdn",
			          "value": f"2{invited_number}"#f"2{invited_number}"
			        }
			      ]
			    }
			  ]
			}
			

		res=requests.post (url0,headers=headers0,json=data0).text
			
			#if (res[''])
			#print (res['reason'])
		if  "3G Customers Not Eligible" in res:
			print ("oops ! , Can't Invite This Customer")
			#elif res.json()['code']=='2037' or (res.text)=='Capping limit exceed':
			#	print ('oops ! ,Done Invited This Number Before !')
		else:
			print ('Congratulations , Done Invited This Customer')			
	
if __name__=="__main__":
		thread = []
		for i in range(10):
			thread1 =threading.Thread(target=all)
			thread1.start()
			thread.append(thread1)
		for thread2 in thread:
			thread1.join 