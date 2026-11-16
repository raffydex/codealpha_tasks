""" BASIC CHATBOT BUILT FOR CodeAlpha PROJECT """

import random

# Welcome function
def welcome():
    """Prints the welcome message"""
    print("===================================")
    print("       WELCOME TO MY CHATBOT")
    print("===================================")
    print("\nChatbot: Hello! How can I help you?")
    print("Chatbot: You can talk to me")
    print("Chatbot: Type 'help'/'assist'/'support' to see what I understand")
    print("Chatbot: Type 'bye'/'exit'/'end' to end the conversation")


# Chatbot function
def chatbot():
    """Main chatbot function"""
    user_name = ""
    message_count = 0

    # Conversation loop
    while True:

        user_input = input("\nYou: ").strip().lower()

        # Input validation
        if user_input == "":
            print("ChatBot: Please enter a message")
            continue

        # Count messages
        message_count += 1

        # Input normalisation
        user_input = " ".join(user_input.split())
        user_input = user_input.rstrip("!?.,").strip()

        # Exit command
        if user_input in ["bye", "goodbye", "exit", "stop", "leave", "end", "bye bye", "end conversation"]:
            print("ChatBot: Goodbye! Have a nice day")
            print("Messages sent:", message_count)
            break

        # Help command
        elif user_input in ["help", "assistance", "support", "service", "assist"]:
            print("\nChatBot: Here are some things you can ask me:")
            print("- Hello, hi, hey")
            print("- How are you?")
            print("- What is your name?")
            print("- My name is ...")
            print("- Call me ...")
            print("- I am ...")
            print("- Thank you")
            print("- I am happy, sad or bored")
            print("- What can you do?")
            print("- Bye")

        # Restart command
        elif user_input == "restart":
            user_name = ""
            message_count = 0
            print("ChatBot: Conversation restarted!")
            print("ChatBot: Hello again! How can I help you?")
            print("Messages sent:", message_count)
            continue

        # Check user input and respond

        # Multiple greetings
        elif user_input in ["hello", "hi", "hey", "hello there", "wassup", "wassup bro", "hyd", "how far", "how far bro"]:
            replies = [
                "Hello! Nice to meet you",
                "Hey! How are you doing?",
                "Hi there! Welcome",
                "Hello! How can I help you?"
            ]
            print("ChatBot:", random.choice(replies))

        # Time-related greetings
        elif user_input in ["good morning", "morning", "good day"]:
            print("ChatBot: Good morning! Have a wonderful day")

        elif user_input in ["good afternoon", "afternoon"]:
            print("ChatBot: Good afternoon! How is your day going?")

        elif user_input in ["good evening", "evening"]:
            print("ChatBot: Good evening! How was your day?")

        elif user_input in ["good night", "night"]:
            print("ChatBot: Good night! Sleep well")

        # Name recognition
        elif user_input.startswith("my name is ") or user_input.startswith("my name's "):
            if user_input.startswith("my name is "):
                new_name = user_input.replace("my name is ", "", 1).strip()
            else:
                new_name = user_input.replace("my name's ", "", 1).strip()

            if new_name and new_name.replace(" ", "").isalpha():
                user_name = new_name.title()
                print("ChatBot: Nice to meet you,", user_name + "!")
            else:
                print("ChatBot: Please enter a valid name")

        # Alternative name introduction
        elif user_input.startswith("call me "):
            new_name = user_input.replace("call me ", "", 1).strip()

            if new_name and new_name.replace(" ", "").isalpha():
                user_name = new_name.title()
                print("ChatBot: Nice to meet you,", user_name + "!")
            else:
                print("ChatBot: Please enter a valid name")

        # Personalised responses
        elif user_input in ["what is my name", "do you know my name", "do you remember my name"]:
            if user_name:
                print("ChatBot: Your name is", user_name)
            else:
                print("ChatBot: You haven't told me your name yet")

        # Asking about the chatbot
        elif user_input in ["how are you", "how are you doing", "are you okay", "hyd", "wassup"]:
            replies = [
                "I am fine, thanks!",
                "I am doing great!",
                "I'm good! How about you?",
                "I'm functioning perfectly. Thanks for asking!"
            ]
            print("ChatBot:", random.choice(replies))

        # Chatbot identity
        elif user_input in ["what is your name", "who are you", "may i know you", "what should i address you as", "who are u"]:
            print("ChatBot: I am ChatBot, your friendly chatbot")

        # Thank-you recognition
        elif user_input in ["thank you", "thanks", "thanks a lot", "i really appreciate", "i really appreciate it", "tnx", "thanks bro", "thank you so much", "thank u"]:
            print("ChatBot: You're welcome! Happy to help")

        elif user_input == "please":
            print("ChatBot: Of course! How can I help?")

        elif user_input in ["help me", "i need your help", "i need ur help", "i need ur assistance"]:
            print("ChatBot: Of course! How can I be of help to you?")
            print("ChatBot: Type 'help'/'assist'/'support' to see what I understand")

        # Basic questions
        elif user_input in ["what can you do", "what do you do"]:
            print("ChatBot: I can chat with you using predefined responses")

        elif user_input == "can you help me":
            print("ChatBot: Of course! Type 'help' to see what I understand")

        # Feelings
        elif user_input in ["i am happy", "i'm happy"]:
            print("ChatBot: That's wonderful! Keep smiling")

        elif user_input in ["i am sad", "i'm sad"]:
            print("ChatBot: Sorry to hear that. I hope things get better")

        elif user_input in ["i am bored", "i'm bored"]:
            print("ChatBot: Maybe try learning something interesting!")

        elif user_input in ["i am fine", "i'm fine", "i am good", "i'm good"]:
            print("ChatBot: Glad to hear that!")

        # Handle unknown messages
        else:
            print("ChatBot: Sorry, I don't understand that yet")

        # Conversation counter
        print("Messages sent:", message_count)


# Start the chatbot
welcome()
chatbot()
