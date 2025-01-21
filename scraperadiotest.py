from bs4 import BeautifulSoup
import requests
import json

response = requests.get('https://www.skyradio.nl/playlist/sky-radio')
print (response.status_code)

soep = BeautifulSoup(response.text)

dingen = soep.select(".mui-j7qwjs")
for t in dingen:
    nummer = t.contents[0].get_text()
    artiest = t.contents[1].get_text()
    print(nummer, artiest)