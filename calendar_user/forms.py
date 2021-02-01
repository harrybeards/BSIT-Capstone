from django import forms
from django.forms import ModelForm
from .models import Meal
from .widgets import FengyuanChenDatePickerInput, WickedPicker


class AddMealForm(ModelForm):
    day = forms.DateField(input_formats=['%d/%m/%Y'],
                          widget=FengyuanChenDatePickerInput())
    start_time = forms.TimeInput(input_formats=['%H:%M %p'],
                                 widget=WickedPicker(), localize=True)
    end_time = forms.TimeInput(input_formats=['%H:%M %p'],
                                 widget=WickedPicker())

    # widgets = {
    #     'day': forms.SelectDateWidget(
    #         empty_label=("Choose Year", "Choose Month", "Choose Day"),
    #     )
    # }

    class Meta:
        model = Meal
        fields = ['title', 'day', 'start_time', 'end_time', 'notes']