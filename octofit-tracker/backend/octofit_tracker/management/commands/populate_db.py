from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            User(email='tony@stark.com', name='Iron Man', team='Marvel'),
            User(email='steve@rogers.com', name='Captain America', team='Marvel'),
            User(email='bruce@wayne.com', name='Batman', team='DC'),
            User(email='clark@kent.com', name='Superman', team='DC'),
        ]
        for user in users:
            user.save()

        # Create activities
        activities = [
            Activity(user_email='tony@stark.com', type='Running', duration=30),
            Activity(user_email='steve@rogers.com', type='Cycling', duration=45),
            Activity(user_email='bruce@wayne.com', type='Swimming', duration=60),
            Activity(user_email='clark@kent.com', type='Flying', duration=120),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=180)

        # Create workouts
        workouts = [
            Workout(name='Hero HIIT', difficulty='Hard'),
            Workout(name='Power Yoga', difficulty='Medium'),
            Workout(name='Speed Run', difficulty='Easy'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
