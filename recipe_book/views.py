from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from recipe_book import models

# Create your views here.


@login_required()
def index(request):
    return render(request, 'recipe-book.html')


class RecipeListView(LoginRequiredMixin, generic.ListView):
    model = models.Recipe


class RecipeDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Recipe
    fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']


class RecipeCreate(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']


class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']


class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipe_book:index')
