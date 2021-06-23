from django import forms

data_fields = [
    ('yearpublished', 'Year Published'),
    ('minplayers', 'Min Players'),
    ('maxplayers', 'Max Players'),
    ('playingtime', 'Playing Time'),
    ('minplaytime', 'Min Play Time'),
    ('maxplaytime', 'Max Play Time'),
    ('age', 'Age'),
    ('boardgamepublisher', 'Publisher'),
]

class BGGForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=32)
    x_axis = forms.CharField(label='X-Axis:',
        widget=forms.Select(choices=data_fields))
    y_axis = forms.CharField(label='Y-Axis:',
        widget=forms.Select(choices=data_fields))
