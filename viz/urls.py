from django.urls import path

from . import views

app_name = 'viz'

urlpatterns = [
    path('', views.form, name='form'),
    path('chart', views.chart, name='chart'),
]
