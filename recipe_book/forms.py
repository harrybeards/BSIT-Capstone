from django import forms
from django.forms import ModelForm, modelformset_factory, inlineformset_factory
from .models import Recipe, Ingredient, Direction
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *

# Adding forms dynamically: https://medium.com/all-about-django/adding-forms-dynamically-to-a-django-formset-375f1090c2b0
# Nested forms: https://swapps.com/blog/working-with-nested-forms-with-django/
# https://dev.to/zxenia/django-inline-formsets-with-class-based-views-and-crispy-forms-14o6


# class AddRecipeForm(ModelForm):
#
#     class Meta:
#         model = Recipe
#         fields = ['title',
#                   'description',
#                   'servings',
#                   'prep_time',
#                   'cook_time',
#                   'url']

class AddRecipeForm(ModelForm):

    class Meta:
        model = Recipe
        exclude = ['user', ]

    def __init__(self, *args, **kwargs):
        super(AddRecipeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('title'),
                Field('description'),
                Field('servings'),
                Field('prep_time'),
                Field('cook_time'),
                Field('url'),
                Fieldset('Add Ingredient'), Formset('ingredients'),
                Field('note'),
                HTML('<br>'),
                ButtonHolder(Submit('submit', 'save'))
            )
        )


class AddIngredientForm(ModelForm):

    class Meta:
        model = Ingredient
        exclude = ()


IngredientFormSet = inlineformset_factory(
    Recipe, Ingredient,
    form=AddIngredientForm,
    fields=('name', 'amount'),
    extra=1,
    max_num=100,
    can_delete=True,
)
