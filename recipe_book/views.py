from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from recipe_book import models
from .forms import AddRecipeForm

# Create your views here.


@login_required()
def index(request):
    return render(request, 'recipe-book.html')


class RecipeListView(LoginRequiredMixin, generic.ListView):
    model = models.Recipe
    context_object_name = 'recipes'

    # Using this method ensures that the only recipes that are displayed are the ones associated with each user
    def get_queryset(self):
        return models.Recipe.objects.filter(recipebook=self.request.user.recipebook)


class RecipeDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Recipe
    fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']
    context_object_name = 'recipe'

    def get_queryset(self):
        return models.Recipe.objects.filter(recipebook=self.request.user.recipebook)


class RecipeCreate(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']

    def form_valid(self, form):
        form.instance.recipebook = self.request.user.recipebook
        return super().form_valid(form)


class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']

    def form_valid(self, form):
        form.instance.recipebook = self.request.user.recipebook
        return super().form_valid(form)


class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipe_book:index')

    def form_valid(self, form):
        form.instance.recipebook = self.request.user.recipebook
        return super().form_valid(form)
