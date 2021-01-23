
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