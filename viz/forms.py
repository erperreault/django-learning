from django import forms
from django.utils.safestring import mark_safe

from .data import data_fields
from .data import stat_fields
from .data import chart_types

class BGGForm(forms.Form):
    """The form takes user settings and passes them to Grapher."""
    username = forms.CharField(label=('BoardGameGeek Username:'), max_length=32,
        widget=forms.TextInput(attrs={'color':'#282828'}))

    chart_type = forms.CharField(
        label = mark_safe('<br>Chart Type:'),
        widget = forms.Select(choices=chart_types),
        initial = 'scatter',
        )

    x_axis = forms.CharField(label=mark_safe('<br>X-Axis:'),
        widget=forms.Select(choices=stat_fields+data_fields))

    y_axis = forms.CharField(label=mark_safe('<br>Y-Axis:'),
        widget=forms.Select(choices=stat_fields+data_fields))