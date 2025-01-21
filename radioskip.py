from __future__ import annotations
import urwid
import threading
import requests
import json
from bs4 import BeautifulSoup


def cur538():
    response = requests.get("https://graph.talparad.io/?query=%7B%0A%20%20station(slug%3A%20%22radio-538%22)%20%7B%0A%20%20%20%20title%0A%20%20%20%20playouts(profile%3A%20%22%22%2C%20limit%3A%2010)%20%7B%0A%20%20%20%20%20%20broadcastDate%0A%20%20%20%20%20%20track%20%7B%0A%20%20%20%20%20%20%20%20id%0A%20%20%20%20%20%20%20%20title%0A%20%20%20%20%20%20%20%20artistName%0A%20%20%20%20%20%20%20%20isrc%0A%20%20%20%20%20%20%20%20images%20%7B%0A%20%20%20%20%20%20%20%20%20%20type%0A%20%20%20%20%20%20%20%20%20%20uri%0A%20%20%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20rankings%20%7B%0A%20%20%20%20%20%20%20%20listName%0A%20%20%20%20%20%20%20%20position%0A%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20__typename%0A%20%20%20%20%7D%0A%20%20%20%20__typename%0A%20%20%7D%0A%7D&variables=%7B%7D", headers={"x-api-key": "da2-abza7qpnqbfe5ihpk4jhcslpgy"})
    r = json.loads(response.content)
    dingen = r["data"]["station"]["playouts"]
    t = dingen[0]
    return (t["track"]["title"], t["track"]["artistName"])
    #for t in dingen:
    #    print(t["track"]["title"], t["track"]["artistName"])

def cur10():
    response = requests.get("https://graph.talparad.io/?query=%7B%0A%20%20station(slug%3A%20%22radio-10%22)%20%7B%0A%20%20%20%20title%0A%20%20%20%20playouts(profile%3A%20%22%22%2C%20limit%3A%2010)%20%7B%0A%20%20%20%20%20%20broadcastDate%0A%20%20%20%20%20%20track%20%7B%0A%20%20%20%20%20%20%20%20id%0A%20%20%20%20%20%20%20%20title%0A%20%20%20%20%20%20%20%20artistName%0A%20%20%20%20%20%20%20%20isrc%0A%20%20%20%20%20%20%20%20images%20%7B%0A%20%20%20%20%20%20%20%20%20%20type%0A%20%20%20%20%20%20%20%20%20%20uri%0A%20%20%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20rankings%20%7B%0A%20%20%20%20%20%20%20%20listName%0A%20%20%20%20%20%20%20%20position%0A%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20__typename%0A%20%20%20%20%7D%0A%20%20%20%20__typename%0A%20%20%7D%0A%7D&variables=%7B%7D", headers={"x-api-key": "da2-abza7qpnqbfe5ihpk4jhcslpgy"})
    r = json.loads(response.content)
    dingen = r["data"]["station"]["playouts"]
    t = dingen[0]
    return (t["track"]["title"], t["track"]["artistName"])
    #for t in dingen:
    #    print(t["track"]["title"], t["track"]["artistName"])

def cursky():
    response = requests.get('https://www.skyradio.nl/playlist/sky-radio')
    soep = BeautifulSoup(response.text, "html.parser")
    dingen = soep.select(".mui-j7qwjs")
    t = dingen[0]
    nummer = t.contents[0].get_text()
    artiest = t.contents[1].get_text()
    return (nummer, artiest)
    #for t in dingen:
    #    nummer = t.contents[0].get_text()
    #    artiest = t.contents[1].get_text()
    #    print(nummer, artiest)

def curveronica():
    response = requests.get("https://api.radioveronica.nl/api/nowplaying/playlist?stationKey=veronica&brand=veronica")
    r = json.loads(response.content)
    t = r["tracks"][0]
    return (t["title"], t["artist"])
    #for t in dingen:
    #    print(t["title"], t["artist"])

def curqmusic():
    response = requests.get("https://api.qmusic.nl/2.0/tracks/plays?limit=10&_station_id=qmusic_nl")
    r = json.loads(response.content)
    t = r["played_tracks"][0]
    return (t["title"], t["artist"]["name"])
    #for t in dingen:
    #    print(t["title"], t["artist"]["name"])

def curradio1():
    response = requests.get("https://www.nporadio1.nl/gedraaid")
    soep = BeautifulSoup(response.text, "html.parser")
    t = soep.select(".sc-417f9aed-0")[0]
    nummer = t.contents[2].get_text()
    artiest = t.contents[3].get_text()
    return (nummer, artiest)
    #for t in dingen:
    #    nummer = t.contents[2].get_text()
    #    artiest = t.contents[3].get_text()
    #    print(nummer, artiest)

def curradio2():
    response = requests.get("https://www.nporadio2.nl/gedraaid")
    soep = BeautifulSoup(response.text, "html.parser")
    t = soep.select(".sc-8e7f384d-0")[0]
    nummer = t.contents[2].get_text()
    artiest = t.contents[3].get_text()
    return (nummer, artiest)
    #for t in dingen:
    #    nummer = t.contents[2].get_text()
    #    artiest = t.contents[3].get_text()
    #    print(nummer, artiest)

def cursublime():
    response = requests.get("https://api.radioveronica.nl/api/nowplaying/playlist?stationKey=sublime&brand=sublime")
    r = json.loads(response.content)
    t = r["tracks"][0]
    return (t["title"], t["artist"])
    #for t in dingen:
    #    print(t["title"], t["artist"])

def curslam():
    response = requests.get("https://api.radioveronica.nl/api/nowplaying/playlist?stationKey=slam&brand=slam")
    r = json.loads(response.content)
    t = r["tracks"][0]
    return (t["title"], t["artist"])
    #for t in dingen:
    #    print(t["title"], t["artist"])

def cur3fm():
    response = requests.get("https://www.npo3fm.nl/gedraaid")
    soep = BeautifulSoup(response.text, "html.parser")
    t = soep.select(".sc-8e7f384d-0")[0]
    nummer = t.contents[2].get_text()
    artiest = t.contents[3].get_text()
    return (nummer, artiest)
    #for t in dingen:
    #    nummer = t.contents[2].get_text()
    #    artiest = t.contents[3].get_text()
    #    print(nummer, artiest)

def curradio4():
    response = requests.get("https://www.npoklassiek.nl/gedraaid")
    soep = BeautifulSoup(response.text, "html.parser")
    t = soep.select(".sc-f1f85519-3")[0]
    nummer = t.contents[0].get_text()
    artiest = t.contents[1].get_text()
    return (nummer, artiest)
    #for t in dingen:
    #    nummer = t.contents[2].get_text()
    #    artiest = t.contents[3].get_text()
    #    print(nummer, artiest)

def curradio5():
    response = requests.get("https://www.nporadio5.nl/gedraaid")
    soep = BeautifulSoup(response.text, "html.parser")
    t = soep.select(".sc-417f9aed-0")[0]
    nummer = t.contents[2].get_text()
    artiest = t.contents[3].get_text()
    return (nummer, artiest)
    #for t in dingen:
    #    nummer = t.contents[2].get_text()
    #    artiest = t.contents[3].get_text()
    #    print(nummer, artiest)

def curfunx():
    response = requests.get("https://www.funx.nl/gedraaid")
    soep = BeautifulSoup(response.text, "html.parser")
    t = soep.select(".sc-417f9aed-0")[0]
    nummer = t.contents[2].get_text()
    artiest = t.contents[3].get_text()
    return (nummer, artiest)
    #for t in dingen:
    #    nummer = t.contents[2].get_text()
    #    artiest = t.contents[3].get_text()
    #    print(nummer, artiest)

def cur100nl():
    response = requests.get("https://api.radioveronica.nl/api/nowplaying/playlist?stationKey=100pnl&brand=100nl")
    r = json.loads(response.content)
    t = r["tracks"][0]
    return (t["title"], t["artist"])
    #for t in dingen:
    #    print(t["title"], t["artist"])

def curkink():
    response = requests.get("https://kink.nl/gedraaid/kink")
    soep = BeautifulSoup(response.text, "html.parser")
    t = soep.select(".flex.grow.flex-col.p-1")[0]
    return (t.contents[0].get_text(), t.contents[1].get_text())
    #for t in dingen:
    #    nummer = t.contents[0].get_text()
    #    artiest = t.contents[1].get_text()
    #    print(nummer, artiest)


def curplaceholer():
    return ("nummer", "artiest")


radios = [
    { "name": "Radio538", "getcur": cur538 },
    { "name": "SkyRadio", "getcur": cursky },
    { "name": "Radio10" , "getcur": cur10 },
    { "name": "Veronica", "getcur": curveronica },
    { "name": "Q-Music", "getcur": curqmusic },
    { "name": "Radio 1", "getcur": curradio1 },
    { "name": "Radio 2", "getcur": curradio2 },
    { "name": "Sublime", "getcur": cursublime },
    { "name": "SlamFM", "getcur": curslam },
    { "name": "3FM", "getcur": cur3fm },
    { "name": "NPO klassiek", "getcur": curradio4 },
    { "name": "Radio 5", "getcur": curradio5 },
    { "name": "FunX", "getcur": curfunx },
    { "name": "100% NL", "getcur": cur100nl },
    { "name": "KINK", "getcur": curkink },
    { "name": "Soul Radio", "getcur": curplaceholer },
    { "name": "Arrow Classic Rock", "getcur": curplaceholer },
    { "name": "classicnl", "getcur": curplaceholer },
    { "name": "Studio040", "getcur": curplaceholer },
    { "name": "StuBru", "getcur": curplaceholer },
]



def checkradio(radio):
    cursong = radio["getcur"]()
    if cursong != radio["cursong"]:
        nummer, artiest = cursong
        radio["cursongtext"].set_text(nummer + " - " + artiest)


for radio in radios:
    radio["cursong"] = ""
    radio["cursongtext"] = urwid.Text("test", align="right")
    radio["testi"] = 0


def doe(loop, spul):
    for radio in radios:
        checkradio(radio)
    loop.set_alarm_in(15, doe)





def quit_on_ctrl_q(key: str) -> None:
    if key == "ctrl q":
        raise urwid.ExitMainLoop()


palette = [
    ("key", "light green,bold", "dark blue"),
    ("footer", "default,bold", "dark blue"),
    ("header", "default,bold", "dark blue")
]

radiolistgroup = []
radiolist = [ 
    urwid.Columns([urwid.RadioButton(radiolistgroup, r["name"]), r["cursongtext"]])
    for r in radios ]
radiolistpile = urwid.Pile(radiolist)

header = urwid.AttrMap(urwid.Text("Radioskip2", align="center"), "header")
footer = urwid.AttrMap(urwid.Text(["TODO, en quit is ", ("key", "Ctrl+Q")]), "footer")
frame = urwid.Frame(urwid.Filler(radiolistpile,valign="top"), header=header, footer=footer)

loop = urwid.MainLoop(frame, palette, unhandled_input=quit_on_ctrl_q)


loop.set_alarm_in(0, doe)
loop.run()