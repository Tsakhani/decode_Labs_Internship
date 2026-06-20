"""
This script contains the arm workouts
"""

def arms_beginner(location):

    if location.lower() == "gym":
        print("Dumbell Curls: 3 x 12, " \
        "Tricep Pushdowns: 3 x 12, " \
        "Hammer Curls: 3 x 12"
        )
    elif location.lower() == "home":
        print("Chair Dips: 3 x 10, " \
        "Close-Grip Push Ups: 3 x 10, " \
        "Isometric Arm Holds: 3 x 20 sec"
        )
    return location

def arms_intermediate(location):

    if location.lower() == "gym":
        print("Barbell Curls: 4 x 10, " \
        "Skull Crushers: 3 x 10, " \
        "Hammer Curls: 3 x 12, " \
        "Rope Pushdowns: 3 x 12"
        )
    elif location.lower() == "home":
        print("Chair Dips: 4 x 15, " \
        "Close-Grip Push Ups: 4 x 12, " \
        "Diamond Push Ups: 4 x 12"
        )
    return location

def arms_advancend(location):

    if location.lower() == "gym":
        print("EZ-Bar Curls: 5 x 10, " \
        "Skull Crushers: 4 x 10, " \
        "Weighted Dips: 4 x 10, " \
        "Concentration Curls: 4 x 12"
        )
    elif location.lower() == "home":
        print("Chair Dips: 5 x 15, " \
        "Explosive Push Ups: 4 x 10, " \
        "Diamond Push Ups: 5 x 20"
        )
    return location




