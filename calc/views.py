from django.http import HttpResponse
from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    context = {'now' : now}
    return render(request, 'calc/index.html', context) 