from bs4 import BeautifulSoup
import requests
import json

response = requests.get('http://hiscore.runescape.com/index_lite.ws?player=zezima')
print (response.status_code)


response = requests.get("https://graph.talparad.io/?query=%7B%0A%20%20station(slug%3A%20%22radio-538%22)%20%7B%0A%20%20%20%20title%0A%20%20%20%20playouts(profile%3A%20%22%22%2C%20limit%3A%2010)%20%7B%0A%20%20%20%20%20%20broadcastDate%0A%20%20%20%20%20%20track%20%7B%0A%20%20%20%20%20%20%20%20id%0A%20%20%20%20%20%20%20%20title%0A%20%20%20%20%20%20%20%20artistName%0A%20%20%20%20%20%20%20%20isrc%0A%20%20%20%20%20%20%20%20images%20%7B%0A%20%20%20%20%20%20%20%20%20%20type%0A%20%20%20%20%20%20%20%20%20%20uri%0A%20%20%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20rankings%20%7B%0A%20%20%20%20%20%20%20%20listName%0A%20%20%20%20%20%20%20%20position%0A%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20__typename%0A%20%20%20%20%7D%0A%20%20%20%20__typename%0A%20%20%7D%0A%7D&variables=%7B%7D", headers={"x-api-key": "da2-abza7qpnqbfe5ihpk4jhcslpgy"})
print(response.status_code)

r = json.loads(response.content)
dingen = r["data"]["station"]["playouts"]
for t in dingen:
    print(t["track"]["title"], t["track"]["artistName"])