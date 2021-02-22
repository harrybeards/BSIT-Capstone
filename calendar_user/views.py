from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Meal, Side
from .forms import AddMealForm, SideFormset

# Create your views here.

@login_required()
def json_list(request):
    meals = Meal.objects.filter(calendaruser=request.user.calendaruser)
    json_array = []

    for meal in meals:
        title = meal.title
        start = meal.date
        url = Meal.get_absolute_url(meal)
        json_entry = {'start': start, 'title': title, 'url': url}
        json_array.append(json_entry)

    return JsonResponse(json_array, safe=False)


class CalendarView(LoginRequiredMixin, generic.ListView):
    model = Meal
    template_name = 'calendar_user.html'
    context_object_name = 'meals'

    def get_queryset(self):
        return Meal.objects.filter(calendaruser=self.request.user.calendaruser)


class MealDetail(LoginRequiredMixin, generic.DetailView):
    model = Meal
    fields = ['title', 'date', 'notes']
    context_object_name = 'meal'

    def get_context_data(self, **kwargs):
        data = super(MealDetail, self).get_context_data(**kwargs)
        data['sides'] = SideFormset(instance=self.object)

        return data

    def get_queryset(self):
        return Meal.objects.filter(calendaruser=self.request.user.calendaruser)


class MealCreate(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = AddMealForm

    def get_context_data(self, **kwargs):
        data = super(MealCreate, self).get_context_data(**kwargs)

        if self.request.POST:
            data['sides'] = SideFormset(self.request.POST)
        else:
            data['sides'] = SideFormset(queryset=Side.objects.none())

        return data

    def form_valid(self, form):
        form.instance.calendaruser = self.request.user.calendaruser
        context = self.get_context_data()
        sides = context['sides']

        self.object = form.save()

        if sides.is_valid():
            sides.instance = self.object
            sides.save()

        return super(MealCreate, self).form_valid(form)


class MealUpdate(LoginRequiredMixin, UpdateView):
    model = Meal
    form_class = AddMealForm
    #fields = ['title', 'date', 'notes']

    def get_context_data(self, **kwargs):
        data = super(MealUpdate, self).get_context_data(**kwargs)

        if self.request.POST:
            data['sides'] = SideFormset(self.request.POST, instance=self.object)
        else:
            data['sides'] = SideFormset(instance=self.object)

        return data

    def form_valid(self, form):
        form.instance.calendaruser = self.request.user.calendaruser
        context = self.get_context_data()
        sides = context['sides']

        self.object = form.save()

        if sides.is_valid():
            sides.instance = self.object
            sides.save()

        return super(MealUpdate, self).form_valid(form)


class MealDelete(LoginRequiredMixin, DeleteView):
    model = Meal
    success_url = reverse_lazy('calendar_user:index')

    def form_valid(self, form):
        form.instance.calendaruser = self.request.user.calendaruser
        return super(MealDelete, self).form_valid(form)
