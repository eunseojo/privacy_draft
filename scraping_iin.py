from bs4 import BeautifulSoup
import requests

url = "https://www.creditcardvalidator.org/american-express"
req = requests.get(url)
txt = req.text

soup = BeautifulSoup(txt, features="html.parser")


all = soup.find_all("a")
count = 0
rep = 0
iin = set()
for i in all:
    t = i.text.strip()
    if t:
        ch = t[0]
        if ch.isdigit(): 
            if t in iin: 
                print(t)
                rep += 1
            iin.add(t)
        count += 1

print(count)
print(iin)
print(len(iin))
print(rep)


f = open("iin.txt", "w")

for i in iin:
    if len(i) > 7: print(i)
    else:
        f.write(i)
        f.write("\n")

f.close()
