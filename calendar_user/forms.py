from django import forms
from django.forms import ModelForm
from .models import Meal
from .widgets import BootstrapDateTimePickerInput


class AddMealForm(ModelForm):
    # date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )
    date = forms.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'], widget=BootstrapDateTimePickerInput())

    class Meta:
        model = Meal
        fields = ['title', 'date', 'notes']
