from django.urls import path
from . import views

app_name = 'recipe_book'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='index'),
    path('recipe/create/', views.RecipeCreate.as_view(), name='recipe-create'),
    path('recipe/<uuid:pk>/update/', views.RecipeUpdate.as_view(), name='recipe-update'),
    path('recipe/<uuid:pk>/delete', views.RecipeDelete.as_view(), name='recipe-delete'),
    path('recipe/<uuid:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail')
]
