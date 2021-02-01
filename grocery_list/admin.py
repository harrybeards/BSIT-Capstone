from django.contrib import admin
from .models import UserGroceryListObject, GroceryList, GroceryItem

# Register your models here.

admin.site.register(UserGroceryListObject)
admin.site.register(GroceryList)
admin.site.register(GroceryItem)

