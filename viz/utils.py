import urllib.request as rq
import xml.etree.ElementTree as et
import pandas as pd

def fetch_bgg_data(game_ids: list):
    result = ""
    for v in game_ids:
        result += f'{v},'
    return rq.urlopen(f'https://boardgamegeek.com/xmlapi/boardgame/{result}')

def parse_xml(file):
    cols = ["name", "yearpublished", "minplayers", "maxplayers"]
    rows = []

    tree = et.parse(file)    
    root = tree.getroot()
    for i in root:
        name = i.find("name").text
        year = i.find("yearpublished").text
        minplayers = i.find("minplayers").text
        maxplayers = i.find("maxplayers").text

        rows.append({
            "name": name,
            "yearpublished": year,
            "minplayers": minplayers,
            "maxplayers": maxplayers,
        })

    df = pd.DataFrame(rows, columns=cols)
    return df
