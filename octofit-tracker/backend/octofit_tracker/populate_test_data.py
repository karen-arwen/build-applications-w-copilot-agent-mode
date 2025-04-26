from pymongo import MongoClient
from bson import ObjectId
from datetime import timedelta

def main():
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']

    # Limpa as coleções
    db.users.delete_many({})
    db.teams.delete_many({})
    db.activity.delete_many({})
    db.leaderboard.delete_many({})
    db.workouts.delete_many({})

    # Usuários
    users = [
        {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
        {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
        {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
        {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
        {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
    ]
    db.users.insert_many(users)

    # Times
    team1 = {"_id": ObjectId(), "name": "Blue Team", "members": [u["_id"] for u in users]}
    team2 = {"_id": ObjectId(), "name": "Gold Team", "members": [u["_id"] for u in users]}
    db.teams.insert_many([team1, team2])

    # Atividades
    activities = [
        {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Cycling", "duration": 60*60},
        {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Crossfit", "duration": 2*60*60},
        {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Running", "duration": 1*60*60+30*60},
        {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "Strength", "duration": 30*60},
        {"_id": ObjectId(), "user": users[4]["_id"], "activity_type": "Swimming", "duration": 1*60*60+15*60},
    ]
    db.activity.insert_many(activities)

    # Leaderboard
    leaderboard = [
        {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
        {"_id": ObjectId(), "user": users[1]["_id"], "score": 90},
        {"_id": ObjectId(), "user": users[2]["_id"], "score": 95},
        {"_id": ObjectId(), "user": users[3]["_id"], "score": 85},
        {"_id": ObjectId(), "user": users[4]["_id"], "score": 80},
    ]
    db.leaderboard.insert_many(leaderboard)

    # Workouts
    workouts = [
        {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
        {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
        {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
        {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
        {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
    ]
    db.workouts.insert_many(workouts)

    print("Test data successfully populated in octofit_db!")

if __name__ == "__main__":
    main()
