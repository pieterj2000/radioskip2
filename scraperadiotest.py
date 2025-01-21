from bs4 import BeautifulSoup
import requests
import json
import urllib

#talpa
# response = requests.get("https://graph.talparad.io/?query=%7B%0A%20%20station(slug%3A%20%22radio-10%22)%20%7B%0A%20%20%20%20title%0A%20%20%20%20playouts(profile%3A%20%22%22%2C%20limit%3A%2010)%20%7B%0A%20%20%20%20%20%20broadcastDate%0A%20%20%20%20%20%20track%20%7B%0A%20%20%20%20%20%20%20%20id%0A%20%20%20%20%20%20%20%20title%0A%20%20%20%20%20%20%20%20artistName%0A%20%20%20%20%20%20%20%20isrc%0A%20%20%20%20%20%20%20%20images%20%7B%0A%20%20%20%20%20%20%20%20%20%20type%0A%20%20%20%20%20%20%20%20%20%20uri%0A%20%20%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20rankings%20%7B%0A%20%20%20%20%20%20%20%20listName%0A%20%20%20%20%20%20%20%20position%0A%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20__typename%0A%20%20%20%20%7D%0A%20%20%20%20__typename%0A%20%20%7D%0A%7D&variables=%7B%7D", headers={"x-api-key": "da2-abza7qpnqbfe5ihpk4jhcslpgy"})
# print(response.status_code)
# 
# r = json.loads(response.content)
# dingen = r["data"]["station"]["playouts"]
# for t in dingen:
#     print(t["track"]["title"], t["track"]["artistName"])


#veronica & sublime 
# response = requests.get("https://api.radioveronica.nl/api/nowplaying/playlist?stationKey=veronica&brand=veronica")
# response = requests.get("https://api.radioveronica.nl/api/nowplaying/playlist?stationKey=sublime&brand=sublime")
# r = json.loads(response.content)
# dingen = r["tracks"]
# for t in dingen:
#     print(t["title"], t["artist"])

#qmusic
# response = requests.get("https://api.qmusic.nl/2.0/tracks/plays?limit=10&_station_id=qmusic_nl")
# r = json.loads(response.content)
# dingen = r["played_tracks"]
# for t in dingen:
#     print(t["title"], t["artist"]["name"])


#radio1
# response = requests.get("https://www.nporadio1.nl/gedraaid")
# soep = BeautifulSoup(response.text, "html.parser")
# dingen = soep.select(".sc-417f9aed-0")
# for t in dingen:
#     nummer = t.contents[2].get_text()
#     artiest = t.contents[3].get_text()
#     print(nummer, artiest)

#radio2
# response = requests.get("https://www.nporadio2.nl/gedraaid")
# soep = BeautifulSoup(response.text, "html.parser")
# dingen = soep.select(".sc-8e7f384d-0")
# for t in dingen:
#     nummer = t.contents[2].get_text()
#     artiest = t.contents[3].get_text()
#     print(nummer, artiest)


#kink.nl
# response = requests.get("https://kink.nl/gedraaid/kink")
# soep = BeautifulSoup(response.text, "html.parser")
# dingen = soep.select(".flex.grow.flex-col.p-1")
# for t in dingen:
#     nummer = t.contents[0].get_text()
#     artiest = t.contents[1].get_text()
#     print(nummer, artiest)


#soulradio
# response = requests.get("https://soulradio.nl/nowplaying/parser.php")
# r = json.loads(response.content)
# print(r["titel"], r["artiest"])

#arrow classic rock
# req = urllib.request.Request("https://www.arrow.nl")
# req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0')
# req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8')
# req.add_header('Accept-Language', 'en-US,en;q=0.5')
# response = urllib.request.urlopen(req).read().decode('utf-8')
# soep = BeautifulSoup(response, "html.parser")
# lijst = []
# t = soep.select(".playTracks > tr")[1]
# while t.get_text().strip() != "":
#     #print()
#     #print(t)
#     #print(t.contents)
#     if len(t.contents) == 1:
#         t = t.contents[0]
#         continue
#     tup = (t.contents[1].get_text(), t.contents[2].get_text())
#     if tup[0] != "":
#         #print(tup)
#         lijst.append(tup)
#     t = t.contents[3]
#     #print(t.contents[2].get_text(), t.contents[1].get_text())
# print(lijst)



#classicnl
# response = requests.get("https://www.classic.nl/ajax/load.php?url=https://www.classic.nl/muziek/playlist")
# r = json.loads(response.content)
# dingen = r["main"]["playlist"]
# for t in dingen:
#     print(t["title"], t["composer"])