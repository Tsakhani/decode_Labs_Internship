"""
This script is for all leg workouts
"""

def legs_beginner(location):

    if location.lower() == "gym":
        print("Goblet Squats: 3 x 10, " \
        "Leg Press: 3 x 12, " \
        "Walking Lunges: 3 x 10, " \
        "Calf Raises 3 x 15"
        )
    elif location.lower() == "home":
        print("Bodyweight Squats: 3 x 15, " \
        "Lunges: 3 x 10, " \
        "Glute Bridges: 3 x 15, " \
        "Wall sit: 3 x 20 sec"
        )
    return location

def legs_intermediate(location):

    if location.lower() == "gym":
        print("Barbell Squats: 4 x 8, " \
        "Romanian Deadlifts: 3 x 10, " \
        "Leg Press: 3 x 12, " \
        "Walking Lunges: 3 x 20"
        )
    elif location.lower() == "home":
        print("Jump Squats: 3 x 15, " \
        "Bulgarian Split Squats: 3 x 12, " \
        "Walking Lunges: 3 x 20, " \
        "Glute Bridges: 4 x 20 "
        )
    return location

def legs_advanced(location):

    if location.lower() == "gym":
        print("Back Squats: 5 x 5, " \
        "Romanian Deadlifts: 4 x 12, " \
        "Bulgarian Split Squats: 4 x 12, " \
        "Leg Extensions: 4 x 15"
        )
    elif location.lower() == "home":
        print("Pistol Squat Progressions: 4 x 8, " \
        "Jump Lunges: 4 x 15, " \
        "Bulgarian Split Squats: 4 x 15, " \
        "Wall sit: 4 x 60 sec"
        )
    return location