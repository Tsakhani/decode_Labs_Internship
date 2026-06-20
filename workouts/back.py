""" 
This script is for all back workouts
"""

def back_beginner(location):

    if location.lower() == "gym":
        print("Lat Pulldown: 3 x 10, " \
        "Seated Cable Row: 3 x 10, " \
        "Assisted Pull Ups: 3 x 8, " \
        "Face Pulls 3 x 12"
        )
    elif location.lower() == "home":
        print("Superman Hold: 3 x 20 sec, " \
        "Bird Dogs: 3 x 10, " \
        "Reverse Snow Angels: 3 x 10, " \
        "Superman Pulls: 3 x 12"
        )
    return location

def back_intermediate(location):
     
    if location.lower() == "gym":
        print("Pull Ups: 4 x 8, " \
        "Barbell Rows: 4 x 8, " \
        "Lat Pulldowns: 3 x 10, " \
        "Seated Rows: 3 x 10"
        )
    elif location.lower() == "home":
        print("Superman Raises: 4 x 15, " \
        "Reverse Snow Angels: 4 x 15, " \
        "Bird Dogs: 4 x 12, " \
        "Prone Back Extentions: 3 x 15"
        )
    return location

def back_advanced(location):
     
    if location.lower() == "gym":
        print("Weighted Pull Ups: 5 x 5, " \
        "Barbell Rows: 5 x 8, " \
        "T-Bar Rows: 4 x 8, " \
        "Deadlifts: 4 x 6"
        )
    elif location.lower() == "home":
        print("Superman Hold: 4 x 20 sec, " \
        "Bird Dogs: 4 x 20, " \
        "Reverse Snow Angels: 4 x 15, " \
        "Superman Pulls: 4 x 20"
        )
    return location