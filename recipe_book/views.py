from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
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


# Classes used to actually create full recipe objects
class RecipeCreate(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']

    def get_context_data(self, **kwargs):
        data = super(RecipeCreate, self).get_context_data(**kwargs)
        user = self.request.user

        if self.request.POST:
            data['ingredients'] = IngredientFormset(self.request.POST)
                #queryset=models.Recipe.objects.filter(recipebook=self.request.user.recipebook))
            data['directions'] = DirectionFormset(self.request.POST)
                #queryset=models.Recipe.objects.filter(recipebook=self.request.user.recipebook))
        else:
            data['ingredients'] = IngredientFormset()
                #queryset=models.Recipe.objects.filter(recipebook=self.request.user.recipebook))
            data['directions'] = DirectionFormset()
                #queryset=models.Recipe.objects.filter(recipebook=self.request.user.recipebook))
        return data

    def form_valid(self, form):
        form.instance.recipebook = self.request.user.recipebook
        context = self.get_context_data()
        ingredients = context['ingredients']
        directions = context['directions']

        # self.object is the object being created
        self.object = form.save()

        if ingredients.is_valid():
            ingredients.instance = self.object
            ingredients.save()
        if directions.is_valid():
            directions.instance = self.object
            directions.save()

        return super(RecipeCreate, self).form_valid(form)


# class RecipeCreate(CreateView):
#     model = models.Recipe
#     fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']
#
#     def get(self, request, *args, **kwargs):
#         """
#         Handles GET requests and instantiates blank versions of the form
#         and its inline formsets.
#         """
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         ingredient_form = IngredientFormset()
#         direction_form = DirectionFormset()
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   ingredient_form=ingredient_form,
#                                   direction_form=direction_form))
#
#     def post(self, request, *args, **kwargs):
#         """
#         Handles POST requests, instantiating a form instance and its inline
#         formsets with the passed POST variables and then checking them for
#         validity.
#         """
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         ingredient_form = IngredientFormset(self.request.POST)
#         direction_form = DirectionFormset(self.request.POST)
#         if (form.is_valid() and ingredient_form.is_valid() and
#             direction_form.is_valid()):
#             return self.form_valid(form, ingredient_form, direction_form)
#         else:
#             return self.form_invalid(form, ingredient_form, direction_form)
#
#     def form_valid(self, form, ingredient_form, direction_form):
#         """
#         Called if all forms are valid. Creates a Recipe instance along with
#         associated Ingredients and Instructions and then redirects to a
#         success page.
#         """
#         form.instance.recipebook = self.request.user.recipebook
#         self.object = form.save()
#         ingredient_form.instance = self.object
#         ingredient_form.save()
#         direction_form.instance = self.object
#         direction_form.save()
#         #return HttpResponseRedirect(self.get_success_url())
#         #return redirect('recipe_book:recipe-detail')
#
#     def form_invalid(self, form, ingredient_form, instruction_form):
#         """
#         Called if a form is invalid. Re-renders the context data with the
#         data-filled forms and errors.
#         """
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   ingredient_form=ingredient_form,
#                                   direction_form=instruction_form))


class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']

    def get_context_data(self, **kwargs):
        data = super(RecipeUpdate, self).get_context_data(**kwargs)

        if self.request.POST:
            data['ingredients'] = IngredientFormset(self.request.POST, instance=self.object)
                            #queryset=models.Recipe.objects.filter(recipebook=self.request.user.recipebook))
            data['directions'] = DirectionFormset(self.request.POST, instance=self.object)
                            #queryset=models.Recipe.objects.filter(recipebook=self.request.user.recipebook))
        else:
            data['ingredients'] = IngredientFormset(instance=self.object)
                            #queryset=models.Recipe.objects.filter(recipebook=self.request.user.recipebook))
            data['directions'] = DirectionFormset(instance=self.object)
                            #queryset=models.Recipe.objects.filter(recipebook=self.request.user.recipebook))
        return data

    def form_valid(self, form):
        form.instance.recipebook = self.request.user.recipebook
        context = self.get_context_data()
        ingredients = context['ingredients']
        directions = context['directions']

        self.object = form.save()

        if ingredients.is_valid():
            ingredients.instance = self.object
            ingredients.save()
        if directions.is_valid():
            directions.instance = self.object
            directions.save()

        return super(RecipeUpdate, self).form_valid(form)


class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipe_book:index')
    context_object_name = 'recipe'

    def form_valid(self, form):
        form.instance.recipebook = self.request.user.recipebook
        return super().form_valid(form)
