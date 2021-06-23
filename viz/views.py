from django.http import HttpResponse
from django.shortcuts import render

from .utils import test_render
from .forms import BGGForm

def form(request):
    if request.method == 'POST':
        form = BGGForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            test_render(form.cleaned_data)
            return HttpResponseRedirect('/chart/')

    else:
        form = BGGForm()

    return render(request, 'viz/form.html', {'form':form})

def chart(request):
    return render(request, 'viz/chart.html')
