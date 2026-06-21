"""
This script is a culmination of all possible workouts
"""

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

def arms_advanced(location):

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