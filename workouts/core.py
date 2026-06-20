"""
This script contains all the core/ab workouts
"""

def core_beginner(location):

    if location.lower() == "gym":
        print("Cable Crunches: 3 x 15, " \
        "Hanging Knee Raises: 3 x 10, " \
        "Plank: 3 x 30 sec"
        )
    elif location.lower() == "home":
        print("Plank: 3 x 30 sec, " \
        "Crunches: 3 x 15, " \
        "Bicycle Crunches: 3 x 15"
        )
    return location

def core_intermediate(location):

    if location.lower() == "gym":
        print("Hanging Leg Raises: 4 x 12, " \
        "Cable Crunches: 4 x 15, " \
        "Russian Twists: 3 x 20"
        )
    elif location.lower() == "home":
        print("Plank: 3 x 60 sec, " \
        "Leg Raises: 3 x 15, " \
        "Bicycle Crunches: 3 x 20," \
        "Mountain Climbers: 3 x 30 sec"
        )
    return location

def core_advanced(location):

    if location.lower() == "gym":
        print("Hanging Leg Raises: 5 x 20, " \
        "Cable Crunches: 4 x 20, " \
        "Ab-wheel Rollouts: 4 x 20"
        )
    elif location.lower() == "home":
        print("Plank: 4 x 90 sec, " \
        "Hollow Body Holds: 4 x 45 sec, " \
        "V-Ups: 4 x 20," \
        "Mountain Climbers: 3 x 30 sec"
        )
    return location
