# mood_responses.py

def mood_response(mood):
    mood = mood.lower()
    if mood == 'happy':
        return "Great to hear that you're happy!"
    elif mood == 'sad':
        return "Cheer up! Tomorrow is another day."
    elif mood == 'excited':
        return "That's awesome! Exciting times ahead!"
    else:
        return "Interesting... Tell me more about that."
