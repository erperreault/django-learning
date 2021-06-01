from django.urls import path

from . import views

# create a namespace for this app
app_name = 'calc'

urlpatterns = [
    # path '' = root
    path('', views.current_datetime, name='index'),
]
