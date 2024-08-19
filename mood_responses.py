# mood_responses.py

def mood_response(mood):
    """Return a custom message based on the user's mood."""
    if mood.lower() == 'happy':
        return "Great to hear that you're happy!"
    elif mood.lower() == 'sad':
        return "Cheer up! Tomorrow is another day."
    elif mood.lower() == 'excited':
        return "That's awesome! Exciting times ahead!"
    else:
        return "Interesting... Tell me more about that."
