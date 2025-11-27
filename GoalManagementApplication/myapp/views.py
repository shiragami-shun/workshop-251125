from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404

def root_redirect(request):
	"""ルートURLでログイン画面へリダイレクト"""
	return redirect(reverse("login"))
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.db.models import Avg

from .models import Goal
from .forms import GoalForm

@login_required
def dashboard(request):
	"""Render a dashboard containing: user's goals, progress summary, and others' goals."""
	user = request.user
	my_goals = Goal.objects.filter(user=user)
	# aggregate average progress for user's goals
	my_progress_avg = my_goals.aggregate(avg=Avg("progress"))["avg"] or 0
	completed_count = my_goals.filter(progress__gte=100).count()

	# others' public goals
	others_goals = Goal.objects.filter(private=False).exclude(user=user)

	context = {
		"my_goals": my_goals,
		"my_progress_avg": int(my_progress_avg),
		"completed_count": completed_count,
		"others_goals": others_goals,
	}
	# Use new clean template to avoid corrupted dashboard.html
	return render(request, "myapp/dashboard_v2.html", context)


@login_required
def create_goal(request):
	if request.method == "POST":
		form = GoalForm(request.POST)
		if form.is_valid():
			goal = form.save(commit=False)
			goal.user = request.user
			goal.save()
			return redirect("myapp:dashboard")
	else:
		form = GoalForm()
	return render(request, "myapp/create_goal.html", {"form": form})


def signup(request):
	"""Allow new users to sign up for an account.

	After successful sign up we automatically log in the user and redirect to dashboard.
	"""
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return redirect("myapp:dashboard")
	else:
		form = UserCreationForm()
	return render(request, "registration/signup.html", {"form": form})


@login_required
def goals_list(request):
	my_goals = Goal.objects.filter(user=request.user)
	return render(request, "myapp/goals_list.html", {"my_goals": my_goals})


@login_required
def progress(request):
	my_goals = Goal.objects.filter(user=request.user)
	my_progress_avg = my_goals.aggregate(avg=Avg("progress"))["avg"] or 0
	completed_count = my_goals.filter(progress__gte=100).count()
	return render(
		request,
		"myapp/progress.html",
		{
			"my_goals": my_goals,
			"my_progress_avg": int(my_progress_avg),
			"completed_count": completed_count,
		},
	)


@login_required
def goal_detail(request, pk):
	"""Show the details for a single goal.

	- If the goal is private and the viewer is not the owner, behave as if it does not exist (404).
	- Otherwise render the `goal_detail.html` template with the goal.
	"""
	goal = get_object_or_404(Goal, pk=pk)
	if goal.private and goal.user != request.user:
		raise Http404
	return render(request, "myapp/goal_detail.html", {"goal": goal})
