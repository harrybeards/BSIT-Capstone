from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Meal, Side
from .widgets import BootstrapDateTimePickerInput


class AddMealForm(ModelForm):

    date = forms.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'], widget=BootstrapDateTimePickerInput())

    class Meta:
        model = Meal
        fields = ['title', 'date', 'notes']


class AddSideForm(ModelForm):

    class Meta:
        model = Side
        fields = ['side']


SideFormset = inlineformset_factory(Meal, Side, form=AddSideForm, extra=1, can_delete=True)

