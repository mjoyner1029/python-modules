# main.py
import mood_responses

def main():
    """Main function to interact with the user and display mood responses."""
    mood = input("How are you feeling today? ")
    print(mood_responses.mood_response(mood))

if __name__ == "__main__":
    main()
