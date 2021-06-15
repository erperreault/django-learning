from django.http import HttpResponse
from django.shortcuts import render

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from viz.utils import fetch_data_by_ids, parse_xml, get_game_ids_by_username

games = {
        "Agricola":31260, 
        "Avalon":128882, 
        "Azul":230802, 
        "Keyflower":122515, 
        "Kingdom Builder":107529
}

supported_fields = [
    'yearpublished',
    'minplayers',
    'maxplayers',
    'playingtime',
    'minplaytime',
    'maxplaytime',
    'age',
    'name',
    'description',
    'thumbnail',
    'image',
    'boardgamepublisher',
]

def index(request):
    ids = get_game_ids_by_username('seepieceeggshell')
    games_xml = fetch_data_by_ids(ids)
    fields = ["name", "yearpublished", "minplayers", "maxplayers"]

    df = parse_xml(games_xml, fields)

    print(df)

    sns.scatterplot(data=df, x='yearpublished', y='maxplayers')
    plt.savefig(f'viz/static/viz/test.png') # save as file to be referenced in index.html
    return render(request, 'viz/index.html') 
