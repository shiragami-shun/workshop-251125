from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Goal


User = get_user_model()
class DashboardViewTests(TestCase):
	def setUp(self):
		self.user1 = User.objects.create_user(username="alice", password="pass")
		self.user2 = User.objects.create_user(username="bob", password="pass")

		Goal.objects.create(user=self.user1, title="Goal A", progress=50)
		Goal.objects.create(user=self.user1, title="Goal B", progress=100)
		Goal.objects.create(user=self.user2, title="Public Goal C", progress=10, private=False)
		Goal.objects.create(user=self.user2, title="Private Goal D", progress=30, private=True)

	def test_dashboard_requires_login(self):
		resp = self.client.get(reverse("myapp:dashboard"))
		self.assertEqual(resp.status_code, 302)  # redirect to login

	def test_dashboard_shows_my_goals_and_others_public_goals(self):
		self.client.login(username="alice", password="pass")
		resp = self.client.get(reverse("myapp:dashboard"))
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, "Goal A")
		self.assertContains(resp, "Goal B")
		# Should contain public goal from bob
		self.assertContains(resp, "Public Goal C")
		# Should NOT contain private goal
		self.assertNotContains(resp, "Private Goal D")
		# Validate progress summary (average 75)
		self.assertContains(resp, "平均進捗: <strong>75%</strong>")

	def test_create_goal(self):
		self.client.login(username="alice", password="pass")
		url = reverse("myapp:create_goal")
		resp = self.client.post(url, {"title": "New Goal", "description": "x", "progress": 20, "private": False})
		self.assertEqual(resp.status_code, 302)  # redirect to dashboard
		# new goal created
		self.assertTrue(Goal.objects.filter(user=self.user1, title="New Goal").exists())

	def test_signup(self):
		signup_url = reverse("myapp:signup")
		resp = self.client.get(signup_url)
		self.assertEqual(resp.status_code, 200)
		resp = self.client.post(signup_url, {"username": "charlie", "password1": "complexpass123", "password2": "complexpass123"})
		# Should redirect to dashboard and user created
		self.assertEqual(resp.status_code, 302)
		self.assertTrue(get_user_model().objects.filter(username="charlie").exists())

	def test_login_template_contains_signup_link(self):
		resp = self.client.get(reverse("login"))
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, "アカウント作成")

	def test_nav_contains_items_and_account(self):
		self.client.login(username="alice", password="pass")
		resp = self.client.get(reverse("myapp:dashboard"))
		self.assertContains(resp, "🏁 目標管理")
		self.assertContains(resp, "ホーム")
		self.assertContains(resp, "目標設定")
		self.assertContains(resp, "進捗")
		self.assertContains(resp, "alice")

	def test_goals_and_progress_pages_accessible(self):
		self.client.login(username="alice", password="pass")
		resp = self.client.get(reverse("myapp:goals_list"))
		self.assertEqual(resp.status_code, 200)
		resp = self.client.get(reverse("myapp:progress"))
		self.assertEqual(resp.status_code, 200)

# Create your tests here.
