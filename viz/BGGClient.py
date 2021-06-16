import urllib.request as rq
import xml.etree.ElementTree as et
import pandas as pd

class BGGClient:
    """
    Retrieves and holds a user's game list, returns it in various formats
    and with optional filters.
    """

    def __init__(self, username: str = ''):
        self.username = username
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

        self.ids = ids

        return ids

    def fetch_data_by_ids(self):
        """
        Fetch complete game data for all listed games.

        game_ids ex: [486, 68413, 84015, 840]
        returns: xml string from BGG api
        """

        formatted_ids = ""
        for i in self.ids:
            formatted_ids += f'{i},'
        url = f'https://boardgamegeek.com/xmlapi/boardgame/{formatted_ids}'

        self.collection_xml = rq.urlopen(url)
        return self.collection_xml

    def yield_dataframe(self, fields: list):
        """
        Pull desired fields from provided XML and return a dataframe of the results.

        returns: pandas dataframe
        """

        rows = []
        root = et.parse(self.collection_xml).getroot()

        for item in root:
            entry = {}
            for field in fields:
                try:
                    entry[field] = int(item.find(field).text)
                except Exception as e:
                    # print(e)
                    entry[field] = item.find(field).text
            rows.append(entry)

        df = pd.DataFrame(rows, columns=fields)
        return df
