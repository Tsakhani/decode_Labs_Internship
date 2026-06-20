"""
This script is for all shoulder workouts
"""

def shoulders_beginner(location):

    if location.lower() == "gym":
        print("Shoulder Press Machine: 3 x 10, " \
        "Lateral Raises: 3 x 12, " \
        "Front Raises: 3 x 12"
        )
    elif location.lower() == "home":
        print("Arm Circles: 3 x 30 sec, " \
        "Shoulder Taps: 3 x 15, " \
        "Pike Holds: 3 X 20 sec"
        )
    return location

def shoulders_intermediate(location):

    if location.lower() == "gym":
        print("Overhead Press: 4 x 18, " \
        "Lateral Raises: 3 x 15, " \
        "Rear Delt Flyes: 3 x 15, " \
        "Arnold Press: 3 X 10"
        )
    elif location.lower() == "home":
        print("Pike Push Ups: 4 x 10, " \
        "Shoulder Taps: 4 x 20, " \
        "Plank Up-Downs: 3 x 15"
        )
    return location

def shoulders_advanced(location):

    if location.lower() == "gym":
        print("Barbell Overhead Press: 5 x 12, " \
        "Rear Delt Flyes: 4 x 15, " \
        "Upright Rows: 4 x 15, " \
        "Arnold Press: 4 X 10"
        )
    elif location.lower() == "home":
        print("Elevated Pike Push Ups: 4 x 12, " \
        "Wall Handstand Holds: 4 x 30 sec, " \
        "Handstand Push Ups: 4 x 5"
        )
    return location