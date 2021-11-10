import requests
file = open("getCountry.txt","r")
lines= file.readlines()

for line in lines:
    r = requests.get("http://localhost:1235/flags"+str(line))
    if r.status_code != 400:
        print(line)