from __future__ import annotations
import urwid
import threading
import requests
import json
from bs4 import BeautifulSoup
import urllib
import queue


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
    nummer = t.contents[1].get_text()
    artiest = t.contents[0].get_text()
    return (nummer, artiest)
    #for t in dingen:
    #    nummer = t.contents[2].get_text()
    #    artiest = t.contents[3].get_text()
    #    print(nummer, artiest)

def curradio5():
    response = requests.get("https://www.nporadio5.nl/gedraaid")
    soep = BeautifulSoup(response.text, "html.parser")
    t = soep.select(".sc-8e7f384d-0")[0]
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
    return (t.contents[1].get_text(), t.contents[0].get_text())
    #for t in dingen:
    #    nummer = t.contents[0].get_text()
    #    artiest = t.contents[1].get_text()
    #    print(nummer, artiest)

def cursoul():
    response = requests.get("https://soulradio.nl/nowplaying/parser.php")
    r = json.loads(response.content)
    return (r["titel"], r["artiest"])

def curarrow():
    req = urllib.request.Request("https://www.arrow.nl")
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8')
    req.add_header('Accept-Language', 'en-US,en;q=0.5')
    response = urllib.request.urlopen(req).read().decode('utf-8')
    soep = BeautifulSoup(response, "html.parser")
    lijst = []
    t = soep.select(".playTracks > tr")[1]
    while t.get_text().strip() != "":
        #print()
        #print(t)
        #print(t.contents)
        if len(t.contents) == 1:
            t = t.contents[0]
            continue
        tup = (t.contents[2].get_text(), t.contents[1].get_text())
        if tup[0] != "":
            #print(tup)
            lijst.append(tup)
        t = t.contents[3]
        #print(t.contents[2].get_text(), t.contents[1].get_text())
    return lijst[0]

def curclassicnl():
    response = requests.get("https://www.classic.nl/ajax/load.php?url=https://www.classic.nl/muziek/playlist")
    r = json.loads(response.content)
    t = r["main"]["playlist"][0]
    return (t["title"], t["composer"])
    #for t in dingen:
    #    print(t["title"], t["composer"])

def curstubru():
    data = {"operationName" : "component",
        "query": "query component($componentId: ID!, $lazyItemCount: Int = 10, $after: ID, $before: ID) {\n  component(id: $componentId) {\n    __typename\n    ... on ContainerNavigationItem {\n      __typename\n      objectId\n      componentId\n      title\n      components {\n        __typename\n        ... on Banner {\n          ...bannerFragment\n          __typename\n        }\n        ... on PaginatedTileList {\n          ...basicPaginatedTileListFragment\n          __typename\n        }\n        ... on StaticTileList {\n          ...basicStaticTileListFragment\n          __typename\n        }\n        ... on ElectronicProgramGuideSchedule {\n          ...epgFragment\n          __typename\n        }\n        ... on Chat {\n          chatId\n          maxAge\n          objectId\n          ...componentTrackingDataFragment\n          __typename\n        }\n        ... on HalloKroket {\n          objectId\n          __typename\n        }\n        ... on Text {\n          ...textFragment\n          __typename\n        }\n        ... on PresentersList {\n          objectId\n          presenters {\n            title\n            __typename\n          }\n          __typename\n        }\n        ... on NoContent {\n          ...noContentFragment\n          __typename\n        }\n      }\n    }\n  }\n}\nfragment basicPaginatedTileListFragment on PaginatedTileList {\n  __typename\n  objectId\n  listId\n  bannerSize\n  description\n  displayType\n  maxAge\n  tileVariant\n  tileContentType\n  tileOrientation\n  title\n  actionItems {\n    ...actionItemFragment\n    __typename\n  }\n  paginatedItems(first: $lazyItemCount, after: $after, before: $before) {\n    __typename\n    edges {\n      __typename\n      cursor\n      node {\n        __typename\n        ...tileFragment\n      }\n    }\n    pageInfo {\n      __typename\n      endCursor\n      hasNextPage\n      hasPreviousPage\n      startCursor\n    }\n  }\n  ... on IComponent {\n    ...componentTrackingDataFragment\n    __typename\n  }\n}\nfragment tileFragment on Tile {\n  ... on IIdentifiable {\n    __typename\n    objectId\n  }\n  ... on IComponent {\n    ...componentTrackingDataFragment\n    __typename\n  }\n  ... on ITile {\n    title\n    active\n    accessibilityTitle\n    action {\n      __typename\n      ... on LinkAction {\n        link\n        linkType\n        openExternally\n        __typename\n      }\n    }\n    actionItems {\n      ...actionItemFragment\n      __typename\n    }\n    image {\n      ...imageFragment\n      __typename\n    }\n    primaryMeta {\n      ...metaFragment\n      __typename\n    }\n    secondaryMeta {\n      ...metaFragment\n      __typename\n    }\n    tertiaryMeta {\n      ...metaFragment\n      __typename\n    }\n    indexMeta {\n      __typename\n      type\n      value\n    }\n    statusMeta {\n      __typename\n      type\n      value\n    }\n    labelMeta {\n      __typename\n      type\n      value\n    }\n    __typename\n  }\n  ... on ContentTile {\n    brand\n    brandLogos {\n      ...brandLogosFragment\n      __typename\n    }\n    __typename\n  }\n  ... on BannerTile {\n    backgroundColor\n    brand\n    brandLogos {\n      ...brandLogosFragment\n      __typename\n    }\n    compactLayout\n    description\n    passUserIdentity\n    textTheme\n    titleArt {\n      objectId\n      templateUrl\n      __typename\n    }\n    __typename\n  }\n  ... on EpisodeTile {\n    description\n    available\n    chapterStart\n    episode {\n      __typename\n      objectId\n      program {\n        __typename\n        objectId\n        link\n      }\n    }\n    progress {\n      completed\n      progressInSeconds\n      durationInSeconds\n      __typename\n    }\n    __typename\n  }\n  ... on PodcastEpisodeTile {\n    available\n    description\n    programLink: podcastEpisode {\n      objectId\n      podcastProgram {\n        objectId\n        link\n        __typename\n      }\n      __typename\n    }\n    progress {\n      completed\n      progressInSeconds\n      durationInSeconds\n      __typename\n    }\n    __typename\n  }\n  ... on AudioLivestreamTile {\n    brand\n    brandsLogos {\n      brand\n      brandTitle\n      logos {\n        ...brandLogosFragment\n        __typename\n      }\n      __typename\n    }\n    progress {\n      durationInSeconds\n      progressInSeconds\n      __typename\n    }\n    __typename\n  }\n  ... on LivestreamTile {\n    description\n    progress {\n      durationInSeconds\n      progressInSeconds\n      __typename\n    }\n    __typename\n  }\n  ... on ButtonTile {\n    mode\n    icons {\n      ...iconFragment\n      __typename\n    }\n    __typename\n  }\n  ... on RadioEpisodeTile {\n    available\n    description\n    progress {\n      completed\n      progressInSeconds\n      durationInSeconds\n      __typename\n    }\n    __typename\n  }\n  ... on RadioFragmentTile {\n    progress {\n      completed\n      progressInSeconds\n      durationInSeconds\n      __typename\n    }\n    __typename\n  }\n  ... on SongTile {\n    startDate\n    formattedStartDate\n    endDate\n    description\n    __typename\n  }\n  __typename\n}\nfragment actionItemFragment on ActionItem {\n  __typename\n  objectId\n  accessibilityLabel\n  active\n  mode\n  title\n  themeOverride\n  action {\n    ...actionFragment\n    __typename\n  }\n  icons {\n    ...iconFragment\n    __typename\n  }\n}\nfragment actionFragment on Action {\n  __typename\n  ... on FavoriteAction {\n    id\n    favorite\n    title\n    __typename\n  }\n  ... on ListDeleteAction {\n    listName\n    id\n    listId\n    title\n    __typename\n  }\n  ... on ListTileDeletedAction {\n    listName\n    id\n    listId\n    __typename\n  }\n  ... on LinkAction {\n    linkId\n    link\n    linkType\n    openExternally\n    passUserIdentity\n    zone {\n      preferredZone\n      isExclusive\n      __typename\n    }\n    linkTokens {\n      __typename\n      placeholder\n      value\n    }\n    __typename\n  }\n  ... on ClientDrivenAction {\n    __typename\n    clientDrivenActionType\n  }\n  ... on ShareAction {\n    title\n    url\n    __typename\n  }\n  ... on SwitchTabAction {\n    referencedTabId\n    mediaType\n    link\n    __typename\n  }\n  ... on FinishAction {\n    id\n    __typename\n  }\n}\nfragment iconFragment on Icon {\n  __typename\n  position\n  ... on DesignSystemIcon {\n    value {\n      name\n      __typename\n    }\n    activeValue {\n      name\n      __typename\n    }\n    __typename\n  }\n  ... on ImageIcon {\n    value {\n      srcSet {\n        src\n        format\n        __typename\n      }\n      __typename\n    }\n    activeValue {\n      srcSet {\n        src\n        format\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\nfragment brandLogosFragment on Logo {\n  colorOnColor\n  height\n  mono\n  primary\n  type\n  width\n  __typename\n}\nfragment componentTrackingDataFragment on IComponent {\n  trackingData {\n    data\n    perTrigger {\n      trigger\n      data\n      template {\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\nfragment imageFragment on Image {\n  __typename\n  objectId\n  alt\n  title\n  focusPoint {\n    x\n    y\n    __typename\n  }\n  templateUrl\n}\nfragment metaFragment on MetaDataItem {\n  __typename\n  type\n  value\n  shortValue\n  longValue\n}\nfragment basicStaticTileListFragment on StaticTileList {\n  __typename\n  objectId\n  listId\n  bannerSize\n  displayType\n  maxAge\n  tileVariant\n  tileContentType\n  tileOrientation\n  title\n  actionItems {\n    ...actionItemFragment\n    __typename\n  }\n  items {\n    ...tileFragment\n    __typename\n  }\n  ... on IComponent {\n    ...componentTrackingDataFragment\n    __typename\n  }\n}\nfragment epgFragment on ElectronicProgramGuideSchedule {\n  __typename\n  objectId\n  maxAge\n  current {\n    tile {\n      ...tileFragment\n      __typename\n    }\n    __typename\n  }\n  next {\n    ...basicPaginatedTileListFragment\n    __typename\n  }\n  previous {\n    ...basicPaginatedTileListFragment\n    __typename\n  }\n}\nfragment textFragment on Text {\n  __typename\n  objectId\n  html\n}\nfragment noContentFragment on NoContent {\n  __typename\n  objectId\n  title\n  text\n  backgroundImage {\n    ...imageFragment\n    __typename\n  }\n  mainImage {\n    ...imageFragment\n    __typename\n  }\n  noContentType\n  actionItems {\n    ...actionItemFragment\n    __typename\n  }\n}\nfragment bannerFragment on Banner {\n  __typename\n  objectId\n  accessibilityTitle\n  brand\n  countdown {\n    date\n    __typename\n  }\n  richDescription {\n    __typename\n    text\n  }\n  image {\n    objectId\n    templateUrl\n    alt\n    focusPoint {\n      x\n      y\n      __typename\n    }\n    __typename\n  }\n  title\n  compactLayout\n  textTheme\n  backgroundColor\n  style\n  action {\n    ...actionFragment\n    __typename\n  }\n  actionItems {\n    ...actionItemFragment\n    __typename\n  }\n  titleArt {\n    objectId\n    templateUrl\n    __typename\n  }\n  labelMeta {\n    __typename\n    type\n    value\n  }\n  ... on IComponent {\n    ...componentTrackingDataFragment\n    __typename\n  }\n}",
        "variables":{"componentId":"#Y25pLWFsc3BnfG8lOHxwbGF5bGlzdHxwJS9saXZlc3RyZWFtL2F1ZGlvL3N0dWRpby1icnVzc2VsLz90YWI9cGxheWxpc3Ql",
        "lazyItemCount":100}}
    headers = {'Accept': 'application/json',
                'Content-Type': 'application/json',
                "x-vrt-client-version": "1.5.8",
                "x-vrt-client-name": "WEB"}
    req = urllib.request.Request('https://www.vrt.be/vrtnu-api/graphql/public/v1', json.dumps(data).encode('utf-8'), headers)
    response = urllib.request.urlopen(req).read().decode('utf-8')
    r = json.loads(response)
    r = r["data"]["component"]["components"][0]["paginatedItems"]["edges"]
    #lijst = []
    for t in r:
        q = (t["node"]["title"], t["node"]["description"])
        if q[1] != "":
            return q
    #        lijst.append(q)
    #print(lijst)


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
    { "name": "Soul Radio", "getcur": cursoul },
    { "name": "Arrow Classic Rock", "getcur": curarrow },
    { "name": "classicnl", "getcur": curclassicnl },
    { "name": "Studio040", "getcur": curplaceholer },
    { "name": "StuBru", "getcur": curstubru },
]



def checkradio(radio):
    cursong = radio["getcur"]()
    if cursong != radio["cursong"]:
        nummer, artiest = cursong
        radio["cursongtext"].set_text(nummer + " - " + artiest)

    #TODO als niet hetzelfde nummer is, stop in queue van radio
    #     en als het de huidige radio is (global variable?) ook in
    #     spotify queue stoppen


#TODO random radio kiezen met hotkey r (ook toggle?)
#TODO functionailiteit buttons en dus radio activeren

#TODO bijhouden wanneer spotifyqueue op is (regelmatig checken), en dan naar volgende radiostation gaatn
# daarvoor moeten we wss bijhouden wat de volgende nummer is vanaf begin af aan (en iedere keer als queue leeg is)
# Let op: get users quuee is de volledige queue, niet alleen tijdelijke queue


#TODO beter uitlijnen titels en artiesten, zowel dat die niet wrappen, als dat 
#   titels en artiesten misschien in losse kolommen moeten dan beter uitzicht

#TODO als we queues van méér dan 1 nummer gaan gebruiken, mischien daar ook een counter
# in stoppen. TODO sowieso doen trouwens, 

#TODO fetchen in andere thread (die queue is thread safe toch?)
# (en is die set_text thread safe?)
# want hij is niet responsive terwijl hij bezig is
# dan moet hij alleen in set_alarm_in
# threads starten voor checken, het spotify gebeuren doen, en
# even refreshsen (of doet hij dat automatisch?) 




for radio in radios:
    radio["cursong"] = ""
    radio["cursongtext"] = urwid.Text("test", align="right")
    radio["testi"] = 0
    radio["queue"] = queue.Queue(maxsize=1)


def doe(loop, doeprint):
    for radio in radios:
        if doeprint:
            print("checking:", radio["name"])
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


loop.set_alarm_in(0, doe, True)
loop.run()