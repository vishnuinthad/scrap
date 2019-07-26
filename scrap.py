import requests
from bs4 import beautifulsoup
import json

fungame = []

url="https://www.miniclip.com/games/en/"

page=requests.get(url).content
soup=beautifulsoup(page,'html.parser')
games=soup.find_all('article',class_='slick-slide')

for game in games:
    if 'Play_code' in game['class']:
        continue


picture=game.find('img').findAll(itemprop="image")

mygame=('picture':picture)

fungme.append(mygame)

#print (games[0].prettify())



with open('data.json','w')as outfile:
    json.dump(fungame.outfile)
