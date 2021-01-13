from django.urls import path
from . import views

app_name = 'recipe_book'

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.RecipeListView.as_view(), name='index'),
    path('recipe/create/', views.RecipeCreate.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete', views.RecipeDelete.as_view(), name='recipe-delete')
]