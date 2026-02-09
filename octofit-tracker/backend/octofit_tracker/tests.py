from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team)
        self.assertEqual(str(user), 'testuser')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='Easy')
        self.assertEqual(str(workout), 'Pushups')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team)
        workout = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='Easy')
        activity = Activity.objects.create(user=user, workout=workout, duration=30, calories_burned=100)
        self.assertIn('testuser', str(activity))

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, rank=1)
        self.assertIn('Test Team', str(leaderboard))
