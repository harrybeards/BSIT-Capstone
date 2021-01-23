from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Recipe, Ingredient, Direction, RecipeBook

# https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d


class AddRecipeForm(ModelForm):
    recipe = forms.ModelChoiceField(queryset=Recipe.objects.all())

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']


class AddIngredientForm(ModelForm):

    class Meta:
        model = Ingredient
        fields = ['name', 'amount']

    # def __init__(self, *args, **kwargs):
    #     self.recipe = kwargs.pop('recipe')
    #     super(AddIngredientForm, self).__init__(*args, **kwargs)
    #
    #     if not self.instance:
    #         self.fields['name'].initial = self.recipe.default_name
    #     self.fields['amount'].widget = forms.TextInput(required=False)
    #
    # def save(self, *args, **kwargs):
    #     self.instance.recipe = self.recipe
    #     ingredient = super(AddIngredientForm, self).save(*args, **kwargs)
    #     return ingredient

    # def __init__(self, *args, **kwargs):
    #     self.organizer = kwargs.pop('organizer')
    #     super(MealForm, self).__init__(*args, **kwargs)
    #     if not self.instance:
    #         self.fields['location'].initial = self.organizer.default_location
    #     self.fields['required'].widget = CheckboxInput(required=False)
    #
    # def clean_time(self):
    #     time = self.cleaned_data['time']
    #     # do stuff with the time to put it in UTC based on the user's default timezone and data passed into the form.
    #
    # def save(self, *args, **kwargs):
    #     self.instance.organizer = self.organizer
    #     meal = super(MealForm, self).save(*args, **kwargs)
    #     return meal


IngredientFormset = inlineformset_factory(Recipe, Ingredient, form=AddIngredientForm, extra=1, can_delete=True)


class AddDirectionForm(ModelForm):

    class Meta:
        model = Direction
        fields = ['step_instructions']

    # def __init__(self, *args, **kwargs):
    #     self.recipe = kwargs.pop('recipe')
    #     super(AddDirectionForm, self).__init__(*args, **kwargs)
    #
    #     if not self.instance:
    #         self.fields['step_instructions'].initial = self.recipe.default_step_instructions
    #
    # def save(self, *args, **kwargs):
    #     self.instance.recipe = self.recipe
    #     direction = super(AddDirectionForm, self).save(*args, **kwargs)
    #     return direction


DirectionFormset = inlineformset_factory(Recipe, Direction, form=AddDirectionForm, extra=1, can_delete=True)
