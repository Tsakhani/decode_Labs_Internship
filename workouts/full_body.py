"""
This script is for the full body workouts
"""

def full_body_beginner(location):
    if location.lower() == "gym":
        print(
            "Goblet Squats: 3 x 10, "
            "Machine Chest Press: 3 x 10, "
            "Lat Pulldowns: 3 x 10, "
            "Walking Lunges: 3 x 10, "
            "Plank: 3 x 30 sec"
        )

    elif location.lower() == "home":
        print(
            "Bodyweight Squats: 3 x 15, "
            "Knee Push-Ups: 3 x 10, "
            "Walking Lunges: 3 x 10, "
            "Plank: 3 x 30 sec, "
            "Jumping Jacks: 3 x 20"
        )

    return location

def full_body_intermediate(location):

    if location.lower() == "gym":
        print(
            "Barbell Squats: 4 x 8, "
            "Bench Press: 4 x 8, "
            "Lat Pulldowns: 4 x 10, "
            "Romanian Deadlifts: 3 x 10, "
            "Plank: 3 x 60 sec"
        )

    elif location.lower() == "home":
        print(
            "Push-Ups: 4 x 15, "
            "Bodyweight Squats: 4 x 20, "
            "Walking Lunges: 3 x 20, "
            "Mountain Climbers: 3 x 30 sec, "
            "Plank: 3 x 60 sec"
        )

    return location

def full_body_advanced(location):

    if location.lower() == "gym":
        print(
            "Deadlifts: 5 x 5, "
            "Barbell Squats: 5 x 5, "
            "Bench Press: 5 x 5, "
            "Pull-Ups: 4 x 10, "
            "Farmer's Carry: 4 rounds"
        )

    elif location.lower() == "home":
        print(
            "Burpees: 4 x 15, "
            "Archer Push-Ups: 4 x 10, "
            "Pistol Squats: 4 x 8, "
            "Mountain Climbers: 4 x 45 sec, "
            "Plank: 4 x 90 sec"
        )

    return location