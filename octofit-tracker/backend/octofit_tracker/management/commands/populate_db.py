from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection

from djongo import models

# Example models for demonstration (should be in models.py)
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear collections
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='pass', first_name='Steve', last_name='Rogers'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='pass', first_name='Diana', last_name='Prince'),
        ]

        # Activities
        Activity.objects.create(user='ironman', team='Marvel', activity_type='Run', points=50)
        Activity.objects.create(user='captainamerica', team='Marvel', activity_type='Swim', points=40)
        Activity.objects.create(user='batman', team='DC', activity_type='Bike', points=60)
        Activity.objects.create(user='wonderwoman', team='DC', activity_type='Yoga', points=30)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=90)
        Leaderboard.objects.create(team='DC', points=90)

        # Workouts
        Workout.objects.create(name='Pushups', difficulty='Easy')
        Workout.objects.create(name='Pullups', difficulty='Medium')
        Workout.objects.create(name='Squats', difficulty='Easy')
        Workout.objects.create(name='Deadlift', difficulty='Hard')


        # Djongo does not support raw MongoDB commands. To ensure a unique index on email, run the following in mongosh:
        #   use octofit_db
        #   db.auth_user.createIndex({ "email": 1 }, { unique: true })

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
