from django.forms import ModelForm
from .models import Recipe, Ingredient, Direction

class AddRecipe(ModelForm):
    class Meta:
        model = Recipe
        # CHANGE THIS, __all__ IS INSECURE, USING IT FOR TESTING
        fields = '__all__'
