from django.test import TestCase
from .models import User, Team, Activity, Workout, LeaderboardEntry

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='activityuser')
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, calories_burned=200, date='2024-01-01')
        self.assertEqual(activity.activity_type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.assertEqual(workout.name, 'Pushups')

class LeaderboardEntryModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(username='leaderboarduser')
        entry = LeaderboardEntry.objects.create(user=user, score=100)
        self.assertEqual(entry.score, 100)
