from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils.safestring import mark_safe
from .models import Meal
from .utils import Calendar
import datetime
import calendar

# Create your views here.


class CalendarView(LoginRequiredMixin, generic.ListView):
    model = Meal
    template_name = 'calendar_user.html'
    context_object_name = 'meals'

    def get_queryset(self):
        return Meal.objects.filter(calendaruser=self.request.user.calendaruser)


class MealDetail(LoginRequiredMixin, generic.DetailView):
    model = Meal
    fields = ['title', 'date', 'notes']

    def get_queryset(self):
        return Meal.objects.filter(calendaruser=self.request.user.calendaruser)


class MealCreate(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ['title', 'date', 'notes']

    def form_valid(self, form):
        form.instance.calendaruser = self.request.user.calendaruser
        return super(MealCreate, self).form_valid(form)


class MealUpdate(LoginRequiredMixin, UpdateView):
    model = Meal
    fields = ['title', 'date', 'notes']

    def form_valid(self, form):
        form.instance.calendaruser = self.request.user.calendaruser
        return super(MealUpdate, self).form_valid(form)


class MealDelete(LoginRequiredMixin, DeleteView):
    model = Meal
    success_url = reverse_lazy('calendar_user:index')

    def form_valid(self, form):
        form.instance.calendaruser = self.request.user.calendaruser
        return super(MealDelete, self).form_valid(form)