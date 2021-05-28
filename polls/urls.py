from django.urls import path

from . import views

# create a namespace for this app
app_name = 'polls'

urlpatterns = [
    # path '' = root
    path('', views.IndexView.as_view(), name='index'),

    # call detail function in views.py
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
