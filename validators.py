"""
This script is in charge of validation
"""

VALID_MUSCLE_GROUPS = [
    "chest",
    "back",
    "legs",
    "shoulders",
    "arms",
    "core",
    "full body"
]

def validate_muscle_group( muscle_group):
    return(
        muscle_group.lower() in VALID_MUSCLE_GROUPS
    )

VALID_LEVELS = [
    "beginner",
    "intermediate",
    "advanced"
]

def validate_level(level):

    return (
        level.lower()
        in
        VALID_LEVELS
    )

VALID_LOCATIONS = [
    "gym",
    "home"
]

def validate_location(location):

    return (
        location.lower()
        in
        VALID_LOCATIONS
    )