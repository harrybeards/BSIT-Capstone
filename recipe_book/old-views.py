# class RecipeCreate(LoginRequiredMixin, CreateView):
#     model = models.Recipe
#     fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']
#
#     def get(self, request, *args, **kwargs):
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
#         self.object = form.save()
#         ingredient_form.instance = self.object
#         ingredient_form.save()
#         direction_form.instance = self.object
#         direction_form.save()
#         return HttpResponseRedirect(self.get_success_url())
#
#     def form_invalid(self, form, ingredient_form, direction_form):
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   ingredient_form=ingredient_form,
#                                   instruction_form=direction_form))




# class RecipeCreate(LoginRequiredMixin, CreateView):
#     model = models.Recipe
#     fields = ['title', 'description', 'servings', 'prep_time', 'cook_time', 'url']
#
#     def get_context_data(self, **kwargs):
#         data = super(RecipeCreate, self).get_context_data(**kwargs)
#         user = self.request.user
#
#         if self.request.POST:
#             data['ingredients'] = IngredientFormset(self.request.POST,
#                 queryset=models.Recipe.objects.filter(recipebook=self.request.user.recipebook))
#             data['directions'] = DirectionFormset(self.request.POST,
#                 queryset=models.Recipe.objects.filter(recipebook=self.request.user.recipebook))
#         else:
#             data['ingredients'] = IngredientFormset(
#                 queryset=models.Recipe.objects.filter(recipebook=self.request.user.recipebook))
#             data['directions'] = DirectionFormset(
#                 queryset=models.Recipe.objects.filter(recipebook=self.request.user.recipebook))
#         return data
#
#     def form_valid(self, form):
#         form.instance.recipebook = self.request.user.recipebook
#         context = self.get_context_data()
#         ingredients = context['ingredients']
#         directions = context['directions']
#
#         # self.object is the object being created
#         self.object = form.save()
#
#         if ingredients.is_valid():
#             ingredients.instance = self.object
#             ingredients.save()
#         if directions.is_valid():
#             directions.instance = self.object
#             directions.save()
#
#         return super(RecipeCreate, self).form_valid(form)