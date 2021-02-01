from django.urls import path
from .views import GroceryListView, GroceryListCreate, GroceryListUpdate, GroceryListDelete, GroceryListDetail

app_name = 'grocery_list'

urlpatterns = [
    path('', GroceryListView.as_view(), name='index'),
    path('list/create/', GroceryListCreate.as_view(), name='grocery-list-create'),
    path('list/<uuid:pk>/', GroceryListDetail.as_view(), name='grocery-list-detail'),
    path('list/<uuid:pk>/update/', GroceryListUpdate.as_view(), name='grocery-list-update'),
    path('list/<uuid:pk>/delete/', GroceryListDelete.as_view(), name='grocery-list-delete'),
]
