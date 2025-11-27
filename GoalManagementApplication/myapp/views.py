from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Goal
from .forms import GoalForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def goal_list(request):
    goals = Goal.objects.all()
    return render(request, 'myapp/goal_list.html', {'goals': goals})

def goal_create(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('goal_list')
    else:
        form = GoalForm()
    return render(request, 'myapp/goal_form.html', {'form': form})

def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    return render(request, 'myapp/goal_detail.html', {'goal': goal})

def goal_update(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goal_detail', pk=pk)
    else:
        form = GoalForm(instance=goal)
    return render(request, 'myapp/goal_form.html', {'form': form, 'goal': goal})

def goal_delete(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == 'POST':
        goal.delete()
        return redirect('goal_list')
    return render(request, 'myapp/goal_confirm_delete.html', {'goal': goal})