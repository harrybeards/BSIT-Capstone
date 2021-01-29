from django.urls import path
from . import views

app_name = 'grocery_list'

urlpatterns = [
    path('', views.GroceryListWeekView.as_view(), name='index'),
    path('grocery-list/create/', views.GroceryListWeekCreate.as_view(), name='grocery-list-create'),
    path('grocery-list/<uuid:pk>/update/', views.GroceryListWeekUpdate.as_view(), name='grocery-list-update'),
    path('grocery-list/<uuid:pk>/delete/', views.GroceryListWeekDelete.as_view(), name='grocery-list-delete'),
    path('grocery-list/<uuid:pk>/', views.GroceryListWeekDetailView.as_view(), name='grocery-list-detail'),
]