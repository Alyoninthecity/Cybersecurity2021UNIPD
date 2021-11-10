import requests
from PIL import Image, ImageDraw, ImageFont
import os


def stringToImg(string,fileName):
    img = Image.new('RGB', (253, 53), color='#FFFFFF')
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("Roboto-Regular.ttf", 30)
    d.text((10, 10), string, fill=(0, 0, 0),font=font)
    img.save(fileName, "PNG")

def sendImgRequest(fileName):
    url = "http://localhost:5000/equation"
    files = {"file": open("eqOcr.png","rb")}
    r = requests.post(url,files=files)
    return r

def findIntoRHTML(requestHTML,stringToFind):
    p = requestHTML.text.find(stringToFind)
    t = requestHTML.text
    res = ""
    if p != -1:
        while t[p+len(stringToFind)]!=' ':
            res +=t[p+len(stringToFind)]
            p+=1
    return res

def deleteFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)

f = "eqOcr.png"
stringToImg("ord(x[0]) = 0",f)
search = "that "
i = 1
res = ""
while sendImgRequest(f).text.find(search)!=-1:
    res += chr(int(findIntoRHTML(sendImgRequest(f),search)))
    stringToImg("ord(x["+str(i)+"]) = 0",f)
    i+=1
deleteFile(f)
print(res)
