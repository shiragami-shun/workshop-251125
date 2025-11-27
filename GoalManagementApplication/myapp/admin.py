from django.contrib import admin
from .models import Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
	list_display = ("title", "user", "progress", "private", "updated_at")
	list_filter = ("user", "private", "updated_at")
	search_fields = ("title", "description", "user__username")
