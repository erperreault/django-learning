import urllib.request as rq
import xml.etree.ElementTree as et
import pandas as pd

def render_chart_from_data(dataframe):
    """
    Given pandas dataframe and chart options, return chart image.
    """
