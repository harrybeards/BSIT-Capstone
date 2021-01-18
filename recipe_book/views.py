from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import transaction
from recipe_book import models
from .forms import IngredientFormset, DirectionFormset

# Create your views here.

# https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d


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

    def get_context_data(self, **kwargs):
        data = super(RecipeCreate, self).get_context_data(**kwargs)

        if self.request.POST:
            data['ingredients'] = IngredientFormset(self.request.POST)
            data['directions'] = DirectionFormset(self.request.POST)
        else:
            data['ingredients'] = IngredientFormset()
            data['directions'] = DirectionFormset()
        return data

    def form_valid(self, form):
        form.instance.recipebook = self.request.user.recipebook
        context = self.get_context_data()
        ingredients = context['ingredients']
        directions = context['directions']
        with transaction.atomic():
            self.object = form.save()

            if ingredients.is_valid() and directions.is_valid():
                ingredients.instance = self.object
                directions.instance = self.object
                ingredients.save()
                directions.save()
        return super(RecipeCreate, self).form_valid(form)


class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']

    def get_context_data(self, **kwargs):
        data = super(RecipeUpdate, self).get_context_data(**kwargs)

        if self.request.POST:
            data['ingredients'] = IngredientFormset(self.request.POST, instance=self.object)
            data['directions'] = DirectionFormset(self.request.POST, instance=self.object)
        else:
            data['ingredients'] = IngredientFormset(instance=self.object)
            data['directions'] = DirectionFormset(instance=self.object)
        return data

    def form_valid(self, form):
        form.instance.recipebook = self.request.user.recipebook
        context = self.get_context_data()
        ingredients = context['ingredients']
        directions = context['directions']
        with transaction.atomic():
            self.object = form.save()

            if ingredients.is_valid() and directions.is_valid():
                ingredients.instance = self.object
                directions.instance = self.object
                ingredients.save()
                directions.save()
        return super(RecipeUpdate, self).form_valid(form)


class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipe_book:index')
    context_object_name = 'recipe'

    def form_valid(self, form):
        form.instance.recipebook = self.request.user.recipebook
        return super().form_valid(form)
