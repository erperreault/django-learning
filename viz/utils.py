import urllib.request as rq
import xml.etree.ElementTree as et
import pandas as pd

from viz.BGGClient import BGGClient
from viz.Grapher import Grapher
from viz.test_data import games, supported_fields

def test_render():
    client = BGGClient('seepieceeggshell')
    df = client.yield_dataframe(supported_fields)

    grapher = Grapher(df)
    grapher.scatter('yearpublished', 'maxplayers')
