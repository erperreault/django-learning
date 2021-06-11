import urllib.request as rq
import xml.etree.ElementTree as et
import pandas as pd

def get_game_ids_by_username(username: str):
    """
    Fetch list of all game ids OWNED by given player and return as list.

    returns: list of ids
    """

    data = rq.urlopen(f'https://boardgamegeek.com/xmlapi/collection/{username}?own=1')
    root = et.parse(data).getroot()
    ids = [item.attrib['objectid'] for item in root]

    return ids

def fetch_data_by_ids(game_ids: list):
    """
    Fetch complete game data for all listed games.

    game_ids ex: [486, 68413, 84015, 840]
    returns: xml string from BGG api
    """

    result = ""
    for v in game_ids:
        result += f'{v},'
    return rq.urlopen(f'https://boardgamegeek.com/xmlapi/boardgame/{result}')

def parse_xml(xml_data, fields: list):
    """
    Pull desired fields from provided XML and return a dataframe of the results.

    returns: pandas dataframe
    """

    rows = []
    root = et.parse(xml_data).getroot()

    for item in root:
        entry = {}
        for field in fields:
            try:
                entry[field] = int(item.find(field).text)
            except Exception as e:
                print(e)
                entry[field] = item.find(field).text 
        rows.append(entry)

    df = pd.DataFrame(rows, columns=fields)
    return df
