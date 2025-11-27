from django.db import models
from django.conf import settings
from django.utils import timezone

class Goal(models.Model):
	"""A goal belonging to a user with a progress indicator.

	Fields:
	- user: owner of the goal
	- title: short title
	- description: optional details
	- progress: integer percent 0-100
	- private: when True, others can't see this goal
	- created_at, updated_at timestamps
	"""
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="goals"
	)
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	progress = models.PositiveSmallIntegerField(default=0)
	private = models.BooleanField(default=False)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-updated_at", "title"]

	def __str__(self):
		return f"{self.title} ({self.user})"

	def is_complete(self):
		return self.progress >= 100
