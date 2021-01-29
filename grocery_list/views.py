from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import GroceryListWeek, GroceryItem
from .forms import GroceryItemFormset
# Create your views here.


class GroceryListWeekView(LoginRequiredMixin, generic.ListView):
    model = GroceryListWeek
    context_object_name = 'grocery_list_week'

    def get_queryset(self):
        return GroceryListWeek.objects.filter(grocerylist=self.request.user.grocerylist)


class GroceryListWeekDetailView(LoginRequiredMixin, generic.DetailView):
    model = GroceryListWeek
    fields = ['name', 'date', 'notes']
    context_object_name = 'grocery_list_week'
    
    def get_queryset(self):
        return GroceryListWeek.objects.filter(grocerylist=self.request.user.grocerylist)


class GroceryListWeekCreate(LoginRequiredMixin, CreateView):
    model = GroceryListWeek
    fields = ['name', 'date', 'notes']
    
    def get_context_data(self, **kwargs):
        data = super(GroceryListWeekCreate, self).get_context_data(**kwargs)
        
        if self.request.POST:
            data['grocery_items'] = GroceryItemFormset(self.request.POST)
        else:
            data['grocery_items'] = GroceryItemFormset(GroceryItem.objects.none())
        
        return data
    
    def form_valid(self, form):
        form.instance.grocerylist = self.request.user.grocerylist
        context = self.get_context_data()
        grocery_items = context['grocery_items']
        
        self.object = form.save()
        
        if grocery_items.is_valid():
            grocery_items.instance = self.object
            grocery_items.save()
        
        return super(GroceryListWeekCreate, self).form_valid(form)


class GroceryListWeekUpdate(LoginRequiredMixin, UpdateView):
    model = GroceryListWeek
    fields = ['name', 'date', 'notes']

    def get_context_data(self, **kwargs):
        data = super(GroceryListWeekCreate, self).get_context_data(**kwargs)

        if self.request.POST:
            data['grocery_items'] = GroceryItemFormset(self.request.POST, instance=self.object)
        else:
            data['grocery_items'] = GroceryItemFormset(instance=self.object)

        return data

    def form_valid(self, form):
        form.instance.grocerylist = self.request.user.grocerylist
        context = self.get_context_data()
        grocery_items = context['grocery_items']

        self.object = form.save()

        if grocery_items.is_valid():
            grocery_items.instance = self.object
            grocery_items.save()

        return super(GroceryListWeekUpdate, self).form_valid(form)


class GroceryListWeekDelete(LoginRequiredMixin, generic.DeleteView):
    model = GroceryListWeek
    success_url = reverse_lazy('grocery_list:index')
    context_object_name = 'grocery_list_week'

    def form_valid(self, form):
        form.instance.grocerylist = self.request.user.grocerylist
        return super().form_valid(form)