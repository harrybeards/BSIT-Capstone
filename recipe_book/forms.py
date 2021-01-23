from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Recipe, Ingredient, Direction, RecipeBook

# https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d


class AddRecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']


class AddIngredientForm(ModelForm):

    class Meta:
        model = Ingredient
        fields = ['name', 'amount']

    # def __init__(self, recipe, *args, **kwargs):
    #     super(AddIngredientForm, self).__init__(*args, **kwargs)
    #     self.fields['recipe'].queryset = Recipe.objects.filter(recipebook=recipebook)


IngredientFormset = inlineformset_factory(Recipe, Ingredient, form=AddIngredientForm, extra=1, can_delete=True)


class AddDirectionForm(ModelForm):

    class Meta:
        model = Direction
        fields = ['step_instructions']

    # def __init__(self, recipe, *args, **kwargs):
    #     super(AddDirectionForm, self).__init__(*args, **kwargs)
    #     self.fields['recipe'].queryset = Recipe.objects.filter(recipebook=recipebook)


DirectionFormset = inlineformset_factory(Recipe, Direction, form=AddDirectionForm, extra=1, can_delete=True)
