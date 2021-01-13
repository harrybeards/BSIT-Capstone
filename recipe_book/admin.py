from django.contrib import admin
from .models import RecipeBook, Recipe, Ingredient, Direction

# Register your models here.


admin.site.register(RecipeBook)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Direction)
