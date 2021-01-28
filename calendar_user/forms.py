from django import forms
from django.forms import ModelForm, SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
from .models import Meal


class AddMealForm(ModelForm):
    day = forms.DateField(widget=SelectDateWidget())

    widgets = {
        'day': forms.SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
    }

    class Meta:
        model = Meal
        fields = ['title', 'day', 'start_time', 'end_time', 'notes']