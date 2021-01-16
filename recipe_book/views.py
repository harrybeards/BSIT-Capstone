from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import transaction
from recipe_book import models
from .forms import AddRecipeForm, IngredientFormSet

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
    template_name = 'recipe_book/recipe_create.html'
    form_class = AddRecipeForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(RecipeCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormSet(self.request.POST)
        else:
            data['ingredients'] = IngredientFormSet()
        return data

    def form_valid(self, form):
        #form.instance.recipebook = self.request.user.recipebook
        context = self.get_context_data()
        ingredients = context['ingredients']

        with transaction.atomic():
            form.instance.recipebook = self.request.user
            self.object = form.save()
            if ingredients.is_valid():
                ingredients.instance = self.object
                ingredients.save()
        return super(RecipeCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe_book:recipe-detail', kwargs={'pk': self.object.pk})
# class RecipeCreate(LoginRequiredMixin, CreateView):
#     model = models.Recipe
#     fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']
#
#     def form_valid(self, form):
#         form.instance.recipebook = self.request.user.recipebook
#
#         context = self.request.user.get_context_data()
#         ingredients = context['ingredients']
#         self.request.user.object = form.save()
#         if ingredients.is_valid():
#             ingredients.instance.recipebook = self.request.user.object
#             ingredients.save()
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         # we have to overwrite this method to make sure the formset gets rendered
#         data = super().get_context_data(**kwargs)
#         if self.request.POST:
#             data['ingredients'] = IngredientFormSet(self.request.POST)
#         else:
#             data['ingredients'] = IngredientFormSet()
#         return data

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = models.Recipe
    template_name = 'recipe_book/recipe_create.html'
    form_class = AddRecipeForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(RecipeUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormSet(self.request.POST, instance=self.request.user.object)
        else:
            data['ingredients'] = IngredientFormSet(instance=self.request.user.object)
        return data

    def form_valid(self, form):
        context = self.request.user.get_context_data()
        ingredients = context['ingredients']
        with transaction.atomic():
            form.instance.recipebook = self.request.user.recipebook
            self.request.user.object = form.save()
            if ingredients.is_valid():
                ingredients.instance = self.object
                ingredients.save()
        return super(RecipeCreate, self).form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy('recipe_book:recipe-detail', kwargs={'pk': self.object.pk})

#
#
# class RecipeUpdate(LoginRequiredMixin, UpdateView):
#     model = models.Recipe
#     fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']
#
#     def form_valid(self, form):
#         form.instance.recipebook = self.request.user.recipebook
#
#         context = self.request.user.get_context_data()
#         ingredients = context['ingredients']
#         self.request.user.object = form.save()
#         if ingredients.is_valid():
#             ingredients.instance.recipebook = self.request.user.object
#             ingredients.save()
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         # we need to overwrite get_context_data to make sure that our formset is rendered.
#         # the difference with CreateView is that on this view we pass instance argument
#         # to the formset because we already have the instance created
#         data = super().get_context_data(**kwargs)
#         if self.request.POST:
#             data['ingredients'] = IngredientFormSet(self.request.POST, instance=self.object)
#         else:
#             data['ingredients'] = IngredientFormSet()
#         return data


class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipe_book:index')

    def form_valid(self, form):
        form.instance.recipebook = self.request.user.recipebook
        return super().form_valid(form)
