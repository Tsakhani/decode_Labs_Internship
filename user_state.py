"""
This script sotres each user's current position in the chatbot conversation
This data will reset though when the app restarts
"""

user_states = {}

def create_user_state(user_id):
    """
    Create a new conversation state for a user
    """

    user_states[user_id] = {
        "step": "muscle_group",
        "muscle_group": None,
        "difficulty": None,
        "location": None
    }

def get_user_state(user_id):
    """
    Returns the user's current state
    """
    return user_states.get(user_id)

def update_user_state(user_id, key, value):
    """
    Updates one value inside the user's conversation state
    """

    if user_id in user_states:
        user_states[user_id][key] = value

def reset_user_state(user_id):
    """
    Clears the user's conversation state after their workout is generated
    """

    if user_id in user_states:
        del user_states[user_id]