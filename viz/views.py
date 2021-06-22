from django.http import HttpResponse
from django.shortcuts import render

import numpy as np
import pandas as pd

from viz.utils import test_render

def index(request):
    test_render()
    return render(request, 'viz/index.html')
