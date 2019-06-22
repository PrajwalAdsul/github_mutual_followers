#%%time
from bs4 import BeautifulSoup 
import requests 

#fabpot andrew
name1 = input()
name2 = input()
print()

s = set()

url = "https://github.com/" + name1 + "?tab=followers"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser') 
txtlist1 = soup.find_all("span", class_="f4 link-gray-dark")
list1 = list()
for i in txtlist1:
    i = str(i)
    i = i.split('>')
    i = i[1].split('<')
    i = i[0]
    list1.append(str(i)) 
    s.add(str(i))

url = "https://github.com/" + name2 + "?tab=followers"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser') 
txtlist2 = soup.find_all("span", class_="f4 link-gray-dark") 
list2 =list() 
for i in txtlist2: 
    i = str(i) 
    i = i.split('>') 
    i = i[1].split('<')
    i = i[0] 
    list2.append(str(i))
    if str(i) in s:
        if len(str(i)) > 0:
            print(str(i))
    
