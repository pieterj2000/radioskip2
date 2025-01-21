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
    soep = BeautifulSoup(response.text)
    dingen = soep.select(".mui-j7qwjs")
    t = dingen[0]
    nummer = t.contents[0].get_text()
    artiest = t.contents[1].get_text()
    return (nummer, artiest)
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
    { "name": "Veronica", "getcur": curplaceholer },
    { "name": "Q-Music", "getcur": curplaceholer },
    { "name": "Radio 1", "getcur": curplaceholer },
    { "name": "Radio 2", "getcur": curplaceholer },
    { "name": "Sublime", "getcur": curplaceholer },
    { "name": "SlamFM", "getcur": curplaceholer },
    { "name": "3FM", "getcur": curplaceholer },
    { "name": "Radio 4", "getcur": curplaceholer },
    { "name": "Radio 5", "getcur": curplaceholer },
    { "name": "FunX", "getcur": curplaceholer },
    { "name": "100% NL", "getcur": curplaceholer },
    { "name": "KINK", "getcur": curplaceholer },
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