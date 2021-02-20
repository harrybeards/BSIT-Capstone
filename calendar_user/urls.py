from django.urls import path
from . import views

app_name = 'calendar_user'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='index'),
    path('meal/create/', views.MealCreate.as_view(), name='meal-create'),
    path('meal/<uuid:pk>/update/', views.MealUpdate.as_view(), name='meal-update'),
    path('meal/<uuid:pk>/delete/', views.MealDelete.as_view(), name='meal-delete'),
    path('meal/<uuid:pk>/', views.MealDetail.as_view(), name='meal-detail'),
    path('json_list', views.json_list, name='json-list')
]
