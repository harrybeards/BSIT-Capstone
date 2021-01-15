from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import Recipe, Ingredient, Direction


class AddRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title',
                  'description',
                  'servings',
                  'prep_time',
                  'cook_time',
                  'url']
        """
        labels = {
            'title': 'Title of the recipe',
            'description': 'Description of the recipe',
            'servings': 'Amount of servings the recipe will yield',
            'prep_time': 'Time it will take to prepare the recipe',
            'cook_time': 'Time it will take to cook the recipe',
            'url': 'URL that links to a website the recipe is on',
        }"""
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Recipe name here'
            }
            )
        }


class AddIngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']