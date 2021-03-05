from django.contrib import admin
from .models import Calendar, Meal, Side

# Register your models here.
admin.site.register(Calendar)

admin.site.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time', 'notes']

admin.site.register(Side)
