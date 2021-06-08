import urllib.request as rq
import xml.etree.ElementTree as et
import pandas as pd

def fetch_bgg_data(game_ids: list):
    result = ""
    for v in game_ids:
        result += f'{v},'
    return rq.urlopen(f'https://boardgamegeek.com/xmlapi/boardgame/{result}')

def parse_xml(xml_data):
    cols = ["name", "yearpublished", "minplayers", "maxplayers"]
    rows = []

    root = et.parse(xml_data).getroot()
    for i in root:
        name = i.find("name").text
        year = int(i.find("yearpublished").text)
        minplayers = int(i.find("minplayers").text)
        maxplayers = int(i.find("maxplayers").text)

        rows.append({
            "name": name,
            "yearpublished": year,
            "minplayers": minplayers,
            "maxplayers": maxplayers,
        })

    df = pd.DataFrame(rows, columns=cols)
    return df
