from django.http import HttpResponseRedirect
from django.shortcuts import render

from .BGGClient import BGGClient
from .Grapher import Grapher
from .forms import BGGForm
from .utils import cleanup_old_charts

def form(request):
    if request.method == 'POST':
        form = BGGForm(request.POST)

        if form.is_valid():
            cleanup_old_charts() # remove image files older than 5min from static/viz
            try:
                client = BGGClient(form.cleaned_data['username'])
            except:
                # most errors are either 1- bad username or 2- too frequent requests.
                # 2 can be avoided by saving user XML to db for 5 min; future improvement
                return render(request, 'viz/error.html', {'form':form})

            df = client.yield_dataframe()
            grapher = Grapher(df)

            chart_type = form.cleaned_data['chart_type']
            x_axis = form.cleaned_data['x_axis']
            y_axis = form.cleaned_data['y_axis']
            grapher.render_input(chart_type, x_axis, y_axis)
            fp = grapher.chart_filepath.split('/', 2)[2]
            return render(request, 'viz/chart.html', {'form':form, 'chart_filepath':fp})

        else:
            form = BGGForm()

    else:
        form = BGGForm()

    return render(request, 'viz/form.html', {'form':form})

def chart(request):
    return render(request, 'viz/chart.html')
