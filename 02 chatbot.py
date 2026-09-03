"""
My Assistant - A Rule-Based Chatbot
Task 4: Basic Chatbot | CodeAlpha Python Programming Internship

A simple terminal chatbot that responds to common greetings and
questions using if-elif-else logic. No AI or ML involved.
"""

import time

CHATBOT_NAME = "ChatBot Assistant"

# Keyword lists grouped by topic (makes matching logic short and readable)
GREETING_WORDS = ["hello", "hi", "hey", "good morning", "good evening"]
HOW_ARE_YOU_WORDS = ["how are you", "how're you", "how are u"]
NAME_WORDS = ["your name", "who are you"]
CAPABILITY_WORDS = ["what can you do", "help", "what do you do"]
THANKS_WORDS = ["thank you", "thanks", "thank u"]
EXIT_WORDS = ["bye", "exit", "quit"]


def print_welcome():
    """Display a styled welcome banner when the program starts."""
    print("=" * 50)
    print(f"   🤖  Welcome to CHATBOT ASSISTANT 🤖")
    print("=" * 50)
    print("Hi! this is a friendly rule-based chatbot.")
    print("I can chat about greetings, how I'm doing,")
    print("=" * 50)
    print()


def get_response(user_input):
    """
    Take the user's raw input, clean it up, and return an
    appropriate predefined reply based on keyword matching.
    """
    # Normalize input: remove extra spaces, convert to lowercase
    text = user_input.strip().lower()

    # Handle empty input
    if text == "":
        return "It looks like you didn't type anything. Could you say that again?"

    # Check each category using the 'in' operator on our keyword lists
    if any(word in text for word in GREETING_WORDS):
        return "Hello there! 😊 How can I help you today?"

    elif any(word in text for word in HOW_ARE_YOU_WORDS):
        return "I'm doing great, thanks for asking! How about you?"

    elif any(word in text for word in NAME_WORDS):
        return f"I'm {CHATBOT_NAME}, your friendly terminal chatbot!"

    elif any(word in text for word in CAPABILITY_WORDS):
        return ("I can chat with you about greetings, how I'm doing, "
                "my name, and general small talk. Try saying 'hello'!")

    elif any(word in text for word in THANKS_WORDS):
        return "You're very welcome! 😊"

    else:
        return "Hmm, I didn't quite understand that. Could you rephrase it?"


def is_exit_command(user_input):
    """Check whether the user wants to end the conversation."""
    text = user_input.strip().lower()
    return any(word == text for word in EXIT_WORDS)


def print_goodbye():
    """Display a friendly closing message before the program ends."""
    print()
    print("=" * 50)
    print(f"🤖 {CHATBOT_NAME}: Goodbye! Have a wonderful day ahead! 👋")
    print("=" * 50)


def run_chatbot():
    """Main loop: repeatedly take input and respond until user exits."""
    print_welcome()

    while True:
        user_input = input("You: ")

        if is_exit_command(user_input):
            break

        reply = get_response(user_input)
        print(f"{CHATBOT_NAME}: {reply}")
        print()

    print_goodbye()


if __name__ == "__main__":
    run_chatbot()