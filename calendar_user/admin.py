from django.contrib import admin
from .models import CalendarUser, Meal

# Register your models here.
admin.site.register(CalendarUser)

admin.site.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time', 'notes']
