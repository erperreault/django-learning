from django import forms
from .settings import data_fields

class BGGForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=32)
    x_axis = forms.CharField(label='X-Axis:',
        widget=forms.Select(choices=data_fields))
    y_axis = forms.CharField(label='Y-Axis:',
        widget=forms.Select(choices=data_fields))
