import urllib.request as rq
import xml.etree.ElementTree as et
import pandas as pd

from .data import stat_fields as s_fields
from .data import data_fields as d_fields

stat_fields = [f[0] for f in s_fields]
data_fields = [f[0] for f in d_fields]

class BGGClient:
    """
    Retrieves and holds a user's game list, returns it in various formats
    and with optional filters.
    """

    def __init__(self, username):
        '''
        if username in database:
            if db.creation_time < 5_minutes_ago:
                self.username = db.username
                self.collection_xml = db.xml_data
            

        else:'''
        self.username = username.replace(' ', '%20')
        self.ids = self.fetch_game_ids()
        self.collection_xml = self.fetch_data_by_ids()


    def fetch_game_ids(self):
        """
        Fetch list of all game ids OWNED by given player and return as list.

        returns: list of ids
        """

        data = rq.urlopen(
            f'https://boardgamegeek.com/xmlapi/collection/{self.username}?own=1'
            )

        root = et.parse(data).getroot()

        ids = [item.attrib['objectid'] for item in root]

        return ids

    def fetch_data_by_ids(self):
        """
        Fetch complete game data for all listed games.

        game_ids ex: [486, 68413, 84015, 840]
        returns: xml object from BGG api
        """

        id_list = ''
        for i in self.ids:
            # 8190 is Apache default max URL, this accounts for len of url below
            if len(id_list) + len(i) < 8151:
                id_list += f'{i},'
            else:
                # for extremely large collections, some games will be left off
                # the limit is something like 1400 titles (avg len 5.67...)
                break

        url = f'https://boardgamegeek.com/xmlapi/boardgame/{id_list}?stats=1'

        xml = rq.urlopen(url)

        return xml

    def yield_dataframe(self):
        """
        Pull desired fields from provided XML and return a dataframe of the results.

        returns: pandas dataframe
        """

        rows = []
        root = et.parse(self.collection_xml).getroot()

        for game in root:
            entry = {}
            self.get_stats_for_item(game, entry)
            for name in game.findall('name'):
                if name.get('primary'):
                    entry['name'] = name.text
            for field in data_fields:
                if game.find(field) is not None:
                    try:
                        entry[field] = int(game.find(field).text)
                    except:
                        entry[field] = game.find(field).text
            rows.append(entry)

        df = pd.DataFrame(rows, columns=data_fields+stat_fields)

        return df

    def get_stats_for_item(self, game, entry):
        for stat in game.findall('statistics'):
            for each in stat.iter():
                if each.tag in stat_fields:
                    try:
                        entry[each.tag] = int(each.text)
                    except ValueError:
                        entry[each.tag] = float(each.text)
