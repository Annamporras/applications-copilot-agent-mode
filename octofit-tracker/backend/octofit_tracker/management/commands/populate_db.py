from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB directly for index creation
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        # Ensure unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Teams
        marvel_team = {'name': 'Team Marvel'}
        dc_team = {'name': 'Team DC'}
        marvel_team_id = db.teams.insert_one(marvel_team).inserted_id
        dc_team_id = db.teams.insert_one(dc_team).inserted_id

        # Users (super heroes)
        users = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team_id': marvel_team_id},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team_id': marvel_team_id},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team_id': dc_team_id},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team_id': dc_team_id},
        ]
        user_ids = db.users.insert_many(users).inserted_ids

        # Activities
        activities = [
            {'user_id': user_ids[0], 'type': 'run', 'distance_km': 5, 'duration_min': 30},
            {'user_id': user_ids[1], 'type': 'cycle', 'distance_km': 20, 'duration_min': 60},
            {'user_id': user_ids[2], 'type': 'swim', 'distance_km': 2, 'duration_min': 40},
            {'user_id': user_ids[3], 'type': 'run', 'distance_km': 10, 'duration_min': 50},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'user_id': user_ids[0], 'points': 100},
            {'user_id': user_ids[1], 'points': 90},
            {'user_id': user_ids[2], 'points': 110},
            {'user_id': user_ids[3], 'points': 95},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {'user_id': user_ids[0], 'workout': 'Push-ups', 'reps': 50},
            {'user_id': user_ids[1], 'workout': 'Sit-ups', 'reps': 40},
            {'user_id': user_ids[2], 'workout': 'Squats', 'reps': 60},
            {'user_id': user_ids[3], 'workout': 'Pull-ups', 'reps': 30},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
