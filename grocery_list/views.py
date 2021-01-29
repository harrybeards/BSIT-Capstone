from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import GroceryList, GroceryItem
from .forms import GroceryItemFormset
# Create your views here.


class GroceryListView(LoginRequiredMixin, generic.ListView):
    model = GroceryList
    context_object_name = 'grocery_list'

    def get_queryset(self):
        return GroceryList.objects.filter(usergrocerylistobject=self.request.user.usergrocerylistobject)


class GroceryListDetail(LoginRequiredMixin, generic.DetailView):
    model = GroceryList
    fields = ['name', 'date', 'notes']
    context_object_name = 'grocery_list'

    def get_context_data(self, **kwargs):
        data = super(GroceryListDetail, self).get_context_data(**kwargs)
        data['grocery_items'] = GroceryItemFormset(instance=self.object)
        return data
    
    def get_queryset(self):
        return GroceryList.objects.filter(usergrocerylistobject=self.request.user.usergrocerylistobject)


class GroceryListCreate(LoginRequiredMixin, CreateView):
    model = GroceryList
    fields = ['name', 'date', 'notes']
    
    def get_context_data(self, **kwargs):
        data = super(GroceryListCreate, self).get_context_data(**kwargs)
        
        if self.request.POST:
            data['grocery_items'] = GroceryItemFormset(self.request.POST)
        else:
            data['grocery_items'] = GroceryItemFormset(queryset=GroceryItem.objects.none())
        
        return data
    
    def form_valid(self, form):
        form.instance.usergrocerylistobject = self.request.user.usergrocerylistobject
        context = self.get_context_data()
        grocery_items = context['grocery_items']
        
        self.object = form.save()
        
        if grocery_items.is_valid():
            grocery_items.instance = self.object
            grocery_items.save()
        
        return super(GroceryListCreate, self).form_valid(form)


class GroceryListUpdate(LoginRequiredMixin, UpdateView):
    model = GroceryList
    fields = ['name', 'date', 'notes']

    def get_context_data(self, **kwargs):
        data = super(GroceryListUpdate, self).get_context_data(**kwargs)

        if self.request.POST:
            data['grocery_items'] = GroceryItemFormset(self.request.POST, instance=self.object)
        else:
            data['grocery_items'] = GroceryItemFormset(instance=self.object)

        return data

    def form_valid(self, form):
        form.instance.usergrocerylistobject = self.request.user.usergrocerylistobject
        context = self.get_context_data()
        grocery_items = context['grocery_items']

        self.object = form.save()

        if grocery_items.is_valid():
            grocery_items.instance = self.object
            grocery_items.save()

        return super(GroceryListUpdate, self).form_valid(form)


class GroceryListDelete(LoginRequiredMixin, DeleteView):
    model = GroceryList
    success_url = reverse_lazy('grocery_list:index')
    context_object_name = 'grocery_list'

    def form_valid(self, form):
        form.instance.usergrocerylistobject = self.request.user.usergrocerylistobject
        return super().form_valid(form)