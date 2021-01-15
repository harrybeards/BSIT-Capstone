from django import forms
from django.forms import ModelForm
from .models import Recipe, Ingredient, Direction


class AddRecipe(ModelForm):
    class Meta:
        model = Recipe
        # CHANGE THIS, __all__ IS INSECURE, USING IT FOR TESTING
        fields = ['title',
                  'description',
                  'servings',
                  'prep_time',
                  'cook_time',
                  'url']
