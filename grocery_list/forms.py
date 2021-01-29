from django.forms import ModelForm, inlineformset_factory
from .models import GroceryListWeek, GroceryItem


class AddGroceryListWeekForm(ModelForm):

    class Meta:
        model = GroceryListWeek
        fields = ['name', 'date', 'notes']


class AddGroceryItemForm(ModelForm):

    class Meta:
        model = GroceryItem
        fields = ['name', 'amount', 'url']


GroceryItemFormset = inlineformset_factory(
    AddGroceryListWeekForm, AddGroceryItemForm,
    form=AddGroceryItemForm, extra=1, can_delete=True)