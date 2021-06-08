from django.http import HttpResponse
from django.shortcuts import render

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from viz.utils import fetch_bgg_data, parse_xml

games = {"Agricola":31260, "Avalon":128882, "Azul":230802, "Keyflower":122515, "Kingdom Builder":107529}

def index(request):
    df = parse_xml(fetch_bgg_data(games.values()))

    print(df)

    sns.scatterplot(data=df, x='yearpublished', y='maxplayers')
    plt.savefig(f'viz/static/viz/test.png') # save file to be referenced in index.html
    return render(request, 'viz/index.html') 