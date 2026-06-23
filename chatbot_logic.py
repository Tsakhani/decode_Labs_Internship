"""
chatbot_logic.py

This file controls the conversation flow of the Telegram Workout Assistant.

It does NOT deal directly with Telegram.
It only receives a user_id and message, then returns the correct response.

Conversation Flow:

User: start
Bot: Which muscle group?

User: Chest
Bot: Beginner, Intermediate, or Experienced?

User: Intermediate
Bot: Gym or Home?

User: Home
Bot: Returns the correct workout
"""

from io import StringIO
from contextlib import redirect_stdout

from user_state import (
    create_user_state,
    get_user_state,
    update_user_state,
    reset_user_state
)

from validators import (
    normalize_input,
    normalize_muscle_group,
    normalize_difficulty,
    normalize_location,
    validate_muscle_group,
    validate_difficulty,
    validate_location
)

from workout_database import (
    chest_beginner,
    chest_intermediate,
    chest_advanced,

    back_beginner,
    back_intermediate,
    back_advanced,

    legs_beginner,
    legs_intermediate,
    legs_advanced,

    shoulders_beginner,
    shoulders_intermediate,
    shoulders_advanced,

    arms_beginner,
    arms_intermediate,
    arms_advanced,

    core_beginner,
    core_intermediate,
    core_advanced,

    full_body_beginner,
    full_body_intermediate,
    full_body_advanced
)


def welcome_message():
    """
    Returns the first message the user sees when starting the bot.
    """

    return (
        "Welcome to your Telegram Workout Assistant.\n\n"
        "I can help you create a workout plan based on:\n"
        "- Muscle group\n"
        "- Difficulty level\n"
        "- Gym or home training\n\n"
        "Which muscle group would you like to train?\n\n"
        "Choose one:\n"
        "Chest\n"
        "Back\n"
        "Legs\n"
        "Shoulders\n"
        "Arms\n"
        "Core\n"
        "Full Body"
    )


def ask_for_muscle_group():
    """
    Asks the user to choose a muscle group.
    """

    return (
        "Which muscle group would you like to train?\n\n"
        "Choose one:\n"
        "Chest\n"
        "Back\n"
        "Legs\n"
        "Shoulders\n"
        "Arms\n"
        "Core\n"
        "Full Body"
    )


def ask_for_difficulty():
    """
    Asks the user to choose a difficulty level.
    """

    return (
        "Great. What difficulty level do you want?\n\n"
        "Choose one:\n"
        "Beginner\n"
        "Intermediate\n"
        "Experienced"
    )


def ask_for_location():
    """
    Asks the user whether they are training at the gym or at home.
    """

    return (
        "Perfect. Where will you be training?\n\n"
        "Choose one:\n"
        "Gym\n"
        "Home"
    )


def invalid_muscle_group_message():
    """
    Returns an error message when the user enters an invalid muscle group.
    """

    return (
        "I did not recognize that muscle group.\n\n"
        "Please choose one of the following:\n"
        "Chest\n"
        "Back\n"
        "Legs\n"
        "Shoulders\n"
        "Arms\n"
        "Core\n"
        "Full Body"
    )


def invalid_difficulty_message():
    """
    Returns an error message when the user enters an invalid difficulty level.
    """

    return (
        "I did not recognize that difficulty level.\n\n"
        "Please choose one of the following:\n"
        "Beginner\n"
        "Intermediate\n"
        "Experienced"
    )


def invalid_location_message():
    """
    Returns an error message when the user enters an invalid training location.
    """

    return (
        "I did not recognize that training location.\n\n"
        "Please choose one of the following:\n"
        "Gym\n"
        "Home"
    )


def help_message():
    """
    Returns a simple help message.
    """

    return (
        "Here is how to use this bot:\n\n"
        "1. Type 'start' to begin.\n"
        "2. Choose a muscle group.\n"
        "3. Choose your difficulty level.\n"
        "4. Choose whether you are training at the gym or at home.\n"
        "5. I will generate a workout for you.\n\n"
        "You can type 'exit', 'cancel', or 'stop' at any time to end the current session."
    )


def exit_message(user_id):
    """
    Ends the user's current conversation and clears their saved state.
    """

    reset_user_state(user_id)

    return (
        "Workout session cancelled.\n\n"
        "You can type 'start' whenever you want a new workout."
    )


def display_difficulty(difficulty):
    """
    Converts the internal difficulty name into the user-facing name.

    Internally:
    - experienced becomes advanced

    User-facing:
    - advanced is displayed as Experienced
    """

    if difficulty == "advanced":
        return "Experienced"

    return difficulty.title()


def call_workout_function(workout_function, location):
    """
    Calls a workout function and returns its output.

    This supports workout functions that either:

    1. Return a string:
       return "Push-Ups: 3 x 15"

    2. Print the workout:
       print("Push-Ups: 3 x 15")

    Since some of your earlier examples used print(), this function captures
    printed output and returns it as a Telegram-friendly text response.
    """

    output_buffer = StringIO()

    with redirect_stdout(output_buffer):
        result = workout_function(location)

    printed_output = output_buffer.getvalue().strip()

    if printed_output:
        return printed_output

    if isinstance(result, str):
        return result

    if result is not None:
        return str(result)

    return (
        "The workout function was found, but it did not return any workout text. "
        "Please check that the function either prints or returns the workout."
    )


def get_workout_function(muscle_group, difficulty):
    """
    Finds the correct workout function based on muscle group and difficulty.

    Example:
    muscle_group = "chest"
    difficulty = "intermediate"

    Returns:
    chest_intermediate
    """

    workout_router = {
        "chest": {
            "beginner": chest_beginner,
            "intermediate": chest_intermediate,
            "advanced": chest_advanced
        },

        "back": {
            "beginner": back_beginner,
            "intermediate": back_intermediate,
            "advanced": back_advanced
        },

        "legs": {
            "beginner": legs_beginner,
            "intermediate": legs_intermediate,
            "advanced": legs_advanced
        },

        "shoulders": {
            "beginner": shoulders_beginner,
            "intermediate": shoulders_intermediate,
            "advanced": shoulders_advanced
        },

        "arms": {
            "beginner": arms_beginner,
            "intermediate": arms_intermediate,
            "advanced": arms_advanced
        },

        "core": {
            "beginner": core_beginner,
            "intermediate": core_intermediate,
            "advanced": core_advanced
        },

        "full body": {
            "beginner": full_body_beginner,
            "intermediate": full_body_intermediate,
            "advanced": full_body_advanced
        }
    }

    return workout_router.get(muscle_group, {}).get(difficulty)


def generate_workout_response(muscle_group, difficulty, location):
    """
    Generates the final workout response after the user has selected:
    - muscle group
    - difficulty
    - location
    """

    workout_function = get_workout_function(
        muscle_group,
        difficulty
    )

    if workout_function is None:
        return (
            "Sorry, I could not find a workout for that selection.\n\n"
            "Please type 'start' and try again."
        )

    workout = call_workout_function(
        workout_function,
        location
    )

    return (
        f"Here is your {display_difficulty(difficulty)} "
        f"{muscle_group.title()} workout for {location.title()} training:\n\n"
        f"{workout}"
    )


def process_message(user_id, message):
    """
    Main chatbot function.

    This function receives the user's message and decides what should happen next.
    """

    message = normalize_input(message)

    if message in [
        "hi",
        "hello",
        "hey",
        "start",
        "/start",
        "workout",
        "i want a workout",
        "i need a workout",
        "create workout",
        "make workout"
    ]:
        create_user_state(user_id)
        return welcome_message()

    if message in ["help", "/help"]:
        return help_message()

    if message in ["exit", "quit", "stop", "cancel", "/cancel"]:
        return exit_message(user_id)

    state = get_user_state(user_id)

    if state is None:
        create_user_state(user_id)
        return ask_for_muscle_group()

    current_step = state["step"]

    if current_step == "muscle_group":

        if not validate_muscle_group(message):
            return invalid_muscle_group_message()

        muscle_group = normalize_muscle_group(message)

        update_user_state(
            user_id,
            "muscle_group",
            muscle_group
        )

        update_user_state(
            user_id,
            "step",
            "difficulty"
        )

        return ask_for_difficulty()

    elif current_step == "difficulty":

        if not validate_difficulty(message):
            return invalid_difficulty_message()

        difficulty = normalize_difficulty(message)

        update_user_state(
            user_id,
            "difficulty",
            difficulty
        )

        update_user_state(
            user_id,
            "step",
            "location"
        )

        return ask_for_location()

    elif current_step == "location":

        if not validate_location(message):
            return invalid_location_message()

        location = normalize_location(message)

        update_user_state(
            user_id,
            "location",
            location
        )

        state = get_user_state(user_id)

        muscle_group = state["muscle_group"]
        difficulty = state["difficulty"]
        location = state["location"]

        workout_response = generate_workout_response(
            muscle_group,
            difficulty,
            location
        )

        reset_user_state(user_id)

        return (
            f"{workout_response}\n\n"
            "Type 'start' if you want another workout."
        )

    else:
        reset_user_state(user_id)

        return (
            "Something went wrong with the conversation flow.\n\n"
            "Type 'start' to begin again."
        )