from django.http import HttpResponse
from django.shortcuts import render

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def index(request):
    df = sns.load_dataset('penguins')

    sns.pairplot(df, hue='species')

    plt.savefig('viz/static/viz/test.png')

    return render(request, 'viz/index.html') 