from django.urls import path

from . import views

urlpatterns = [
    # path '' = root
    path('', views.index, name='index'),
]
