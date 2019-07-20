import requests
from bs4 import beautifulsoup
import json

cleanhouses = []

url="https://en.wikipedia.org/wiki/Main_Page"

page=requests.get(url).content
soup=beautifulsoup(page,'html.parser')
houses=soup.find_all('div',class_='thumbinner mp-thumb')
print (houses[0].prettify())



with open('data.json','w')as outfile:
    json.dump(cleanhouse.outfile)