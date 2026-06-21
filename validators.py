"""
validators.py

This file contains all validation and input-normalization logic
for the Telegram Workout Assistant.

Its job is simple:
- Clean user input
- Check if the user selected a valid muscle group
- Check if the user selected a valid difficulty level
- Check if the user selected a valid training location

This file should NOT contain:
- Flask code
- Telegram API code
- Workout routines
- User state logic
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


VALID_DIFFICULTIES = [
    "beginner",
    "intermediate",
    "advanced",
    "experienced"
]


VALID_LOCATIONS = [
    "gym",
    "home"
]


def normalize_input(user_input):
    """
    Cleans the user's input by:
    - Converting it to a string
    - Removing spaces before and after the text
    - Converting it to lowercase

    Example:
    "   Chest   " becomes "chest"
    """

    if user_input is None:
        return ""

    return str(user_input).strip().lower()


def normalize_muscle_group(muscle_group):
    """
    Normalizes muscle group input.

    This is useful because users might type:
    - "fullbody"
    - "full-body"
    - "full_body"

    But your bot should understand all of them as:
    - "full body"
    """

    muscle_group = normalize_input(muscle_group)

    if muscle_group in ["fullbody", "full-body", "full_body", "full body workout"]:
        return "full body"

    if muscle_group in ["abs", "abdominals", "stomach"]:
        return "core"

    if muscle_group in ["arm", "biceps", "triceps", "bicep", "tricep"]:
        return "arms"

    if muscle_group in ["leg", "lower body", "lower-body", "lower_body"]:
        return "legs"

    if muscle_group in ["shoulder", "delts", "deltoids"]:
        return "shoulders"

    return muscle_group


def normalize_difficulty(difficulty):
    """
    Normalizes difficulty input.

    Your previous code uses 'advanced' in the workout router,
    but your project wording uses 'experienced'.

    To avoid breaking the app, this function converts:
    'experienced' into 'advanced'.
    """

    difficulty = normalize_input(difficulty)

    if difficulty in ["experienced", "expert", "hard"]:
        return "advanced"

    if difficulty in ["medium", "normal"]:
        return "intermediate"

    if difficulty in ["easy", "starter", "newbie"]:
        return "beginner"

    return difficulty


def normalize_location(location):
    """
    Normalizes training location input.

    This allows users to type:
    - "no equipment"
    - "bodyweight"
    - "house"

    And the bot still understands the user means:
    - "home"
    """

    location = normalize_input(location)

    if location in [
        "house",
        "at home",
        "home workout",
        "no equipment",
        "without equipment",
        "bodyweight",
        "body weight"
    ]:
        return "home"

    if location in [
        "at gym",
        "the gym",
        "gym workout",
        "equipment",
        "with equipment"
    ]:
        return "gym"

    return location


def validate_muscle_group(muscle_group):
    """
    Checks whether the selected muscle group is valid.
    """

    muscle_group = normalize_muscle_group(muscle_group)

    return muscle_group in VALID_MUSCLE_GROUPS


def validate_difficulty(difficulty):
    """
    Checks whether the selected difficulty level is valid.
    """

    difficulty = normalize_difficulty(difficulty)

    return difficulty in ["beginner", "intermediate", "advanced"]


def validate_location(location):
    """
    Checks whether the selected training location is valid.
    """

    location = normalize_location(location)

    return location in VALID_LOCATIONS


def validate_request(muscle_group, difficulty, location):
    """
    Validates a complete workout request.

    This is optional, but useful if later you want users to type
    everything in one message, such as:

    'chest beginner home'
    """

    return (
        validate_muscle_group(muscle_group)
        and validate_difficulty(difficulty)
        and validate_location(location)
    )