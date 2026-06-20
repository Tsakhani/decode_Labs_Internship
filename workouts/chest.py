"""
The following contains all the chest workouts
"""

def chest_beginner(location):
     
    if location.lower() == "gym":
        print("Bench Press: 3 x 10, " \
        "Incline Dumbell Press: 3 x 10, " \
        "Chest Fly Machine: 3 x 12, " \
        "Push Ups: 2 x 10"
        )
    elif location.lower() == "home":
        print("Knee Push Ups: 3 x 10," \
        "Incline Push Ups: 3 x 10," \
        "Wall Push Ups: 3 x 15," \
        "Chest Hold Plank: 3 x 20 sec")
    return location

def chest_intermediate(location):

    if location.lower() == "gym":
        print("Bench Press: 3 x 8, " \
        "Incline Dumbell Press: 3 x 10, " \
        "Cable Flyes: 3 x 12," \
        "Chest Dips: 3 x 12, " \
        "Push Ups: 3 x 15"
        )
    elif location.lower() == "home":
        print("Standard Push Ups: 4 x 15," \
        "Wide Push Ups: 3 x 12," \
        "Diamond Push Ups: 3 x 10," \
        "Decline Push Ups: 3 x 10")
    return location

def chest_advanced(location):

    if location.lower() == "gym":
        print("Bench Press: 5 x 10, " \
        "Incline Bench Press: 4 x 15, " \
        "Weighted Dips: 4 x 10, " \
        "Cable Flyes: 4 x 15," \
        "Dumbell Pullover: 3 x 12"
        )
    elif location.lower() == "home":
        print("Archer Push Ups: 3 x 10," \
        "Decline Push Ups: 5 x 10," \
        "Plyometric Push Ups: 4 x 8," \
        "Diamond Push Ups: 4 x 15")
    return location

