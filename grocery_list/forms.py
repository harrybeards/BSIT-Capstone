from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import GroceryList, GroceryItem
from .widgets import FengyuanChenDatePickerInput


class AddGroceryListWeekForm(ModelForm):
    date = forms.DateField(input_formats=['%d/%m/%Y'],
                          widget=FengyuanChenDatePickerInput())

    class Meta:
        model = GroceryList
        fields = ['name', 'date', 'notes']


class AddGroceryItemForm(ModelForm):

    class Meta:
        model = GroceryItem
        fields = ['name', 'amount', 'url']


GroceryItemFormset = inlineformset_factory(
    GroceryList, GroceryItem,
    form=AddGroceryItemForm, extra=1, can_delete=True)