from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .BGGClient import BGGClient
from .Grapher import Grapher
from .utils import test_render
from .forms import BGGForm
from .test_data import supported_fields

def form(request):
    if request.method == 'POST':
        form = BGGForm(request.POST)

        if form.is_valid():
            client = BGGClient(form.cleaned_data['username'])
            df = client.yield_dataframe(supported_fields)
            grapher = Grapher(df)

            x_axis = form.cleaned_data['x_axis']
            y_axis = form.cleaned_data['y_axis']
            grapher.scatter(x_axis, y_axis)
            return HttpResponseRedirect('chart')

    else:
        form = BGGForm()

    return render(request, 'viz/form.html', {'form':form})

def chart(request):
    return render(request, 'viz/chart.html')
