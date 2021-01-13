from django.contrib import admin
from .models import GroceryList, GroceryListWeek

# Register your models here.

admin.site.register(GroceryList)
admin.site.register(GroceryListWeek)

