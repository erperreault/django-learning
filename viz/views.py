import pandas as pd

from django.shortcuts import render

from .BGGClient import BGGClient
from .Grapher import Grapher
from .forms import BGGForm
from .models import User
from .utils import cleanup_old_charts, cleanup_old_collections

from datetime import datetime

def form(request):
    # Sets form to a blank BGGForm instance until a valid request is passed.
    if request.method == 'POST':
        form = BGGForm(request.POST)

        if form.is_valid():
            cleanup_old_charts()        # remove chart image files older than 5 minutes
            cleanup_old_collections()   # remove user collections in local db older then 5 minutes

            username = form.cleaned_data['username']

            try:
                user = User.objects.get(username=username)
            except:
                user = False

            if user:
                df = pd.read_json(user.xml_data)    # unpack collection, json -> pandas dataframe
            else:
                try:
                    # if collection not saved in database, fetch from BGG
                    client = BGGClient(form.cleaned_data['username'])
                    df = client.yield_dataframe()
        
                    # pass live data to User instance and save to database
                    user = User()
                    user.username = client.username
                    user.creation_time = datetime.now()
                    user.xml_data = df.to_json()
                    user.save()

                except:
                    # this is usually (always?) caused by a bad username, but keep generic for now
                    return render(request, 'viz/error.html', {'form':form})
                    
            # Grapher will take dataframe and render appropriate chart type with seaborn
            grapher = Grapher(df)
            chart_type = form.cleaned_data['chart_type']
            x_axis = form.cleaned_data['x_axis']
            y_axis = form.cleaned_data['y_axis']
            grapher.set_chart_type(chart_type, x_axis, y_axis)    # saves as file in static/viz
            fp = grapher.chart_filepath.split('/', 2)[2]        # grab just the image key string 
            return render(request, 'viz/chart.html', {'form':form, 'chart_filepath':fp})

        else:
            form = BGGForm()

    else:
        form = BGGForm()

    return render(request, 'viz/form.html', {'form':form})

def chart(request):
    return render(request, 'viz/chart.html')
