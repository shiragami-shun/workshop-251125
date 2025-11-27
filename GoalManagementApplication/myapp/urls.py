
from django.urls import path
from . import views


app_name = "myapp"

urlpatterns = [
    path("", views.root_redirect, name="root_redirect"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/signup/", views.signup, name="signup"),
    path("goals/create/", views.create_goal, name="create_goal"),
    path("goals/<int:pk>/", views.goal_detail, name="goal_detail"),
    path("goals/", views.goals_list, name="goals_list"),
    path("progress/", views.progress, name="progress"),
]
