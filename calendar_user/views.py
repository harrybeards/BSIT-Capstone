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

    def get_context_data(self, **kwargs):
        after_day = self.request.GET.get('day__gte', None)
        context = super().get_context_data(**kwargs)

        if not after_day:
            d = datetime.date.today()
        else:
            try:
                split_after_day = after_day.split('-')
                d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
            except:
                d = datetime.date.today()

        previous_month = datetime.date(year=d.year, month=d.month, day=1)  # find first day of current month
        previous_month = previous_month - datetime.timedelta(days=1)  # backs up a single day
        previous_month = datetime.date(year=previous_month.year, month=previous_month.month,
                                       day=1)  # find first day of previous month

        last_day = calendar.monthrange(d.year, d.month)
        next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])  # find last day of current month
        next_month = next_month + datetime.timedelta(days=1)  # forward a single day
        next_month = datetime.date(year=next_month.year, month=next_month.month,
                                   day=1)  # find first day of next month

        context['previous_month'] = reverse('calendar_user:index') + '?day__gte=' + str(
            previous_month)
        context['next_month'] = reverse('calendar_user:index') + '?day__gte=' + str(next_month)

        cal = Calendar()
        html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
        html_calendar = html_calendar.replace('<td ', '<td  width="150" height="150"')
        context['calendar'] = mark_safe(html_calendar)
        #return super(CalendarView, self).get_context_data(self.request, extra_context)
        return context

    def get_queryset(self):
        return Meal.objects.filter(calendaruser=self.request.user.calendaruser)


class MealDetail(LoginRequiredMixin, generic.DetailView):
    model = Meal
    fields = ['title', 'day', 'start_time', 'end_time', 'notes']

    def get_queryset(self):
        return Meal.objects.filter(calendaruser=self.request.user.calendaruser)


class MealCreate(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ['title', 'day', 'start_time', 'end_time', 'notes']

    def form_valid(self, form):
        form.instance.calendaruser = self.request.user.calendaruser
        return super(MealCreate, self).form_valid(form)


class MealUpdate(LoginRequiredMixin, UpdateView):
    model = Meal
    fields = ['title', 'day', 'start_time', 'end_time', 'notes']

    def form_valid(self, form):
        form.instance.calendaruser = self.request.user.calendaruser
        return super(MealUpdate, self).form_valid(form)


class MealDelete(LoginRequiredMixin, DeleteView):
    model = Meal
    success_url = reverse_lazy('calendar_user:index')

    def form_valid(self, form):
        form.instance.calendaruser = self.request.user.calendaruser
        return super(MealDelete, self).form_valid(form)