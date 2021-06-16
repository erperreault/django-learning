from django.http import HttpResponse
from django.shortcuts import render

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from viz.BGGClient import BGGClient
from viz.Grapher import Grapher
from viz.test_data import games, supported_fields

def index(request):
    client = BGGClient('seepieceeggshell')
    fields = supported_fields

    df = client.yield_dataframe(fields)

    print(df)

    sns.scatterplot(data=df, x='yearpublished', y='maxplayers')
    plt.savefig(f'viz/static/viz/test.png') # save as file to be referenced in index.html
    return render(request, 'viz/index.html')
