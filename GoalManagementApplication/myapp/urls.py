from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/signup/", views.signup, name="signup"),
    path("goals/create/", views.create_goal, name="create_goal"),
    path("goals/", views.goals_list, name="goals_list"),
    path("progress/", views.progress, name="progress"),
]
