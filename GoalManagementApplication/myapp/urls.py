from django.urls import path
from . import views

urlpatterns = [
    path('', views.goal_list, name='goal_list'),
    path('create/', views.goal_create, name='goal_create'),
    path('<int:pk>/', views.goal_detail, name='goal_detail'),
    path('<int:pk>/update/', views.goal_update, name='goal_update'),
    path('<int:pk>/delete/', views.goal_delete, name='goal_delete'),
]