# ai voice assistant bot

import datetime
import webbrowser
import os
import sys

import speech_recognition as sr
import pyttsx3

try:
    import wikipedia
    WIKIPEDIA_AVAILABLE = True
except ImportError:
    WIKIPEDIA_AVAILABLE = False


# 1. INITIAL SETUP(starting)


engine = pyttsx3.init()

# Optional: adjust voice properties
engine.setProperty('rate', 170)     # speaking speed
voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)   # 0 = male, 1 = female (varies by OS)


def speak(text):
    """Convert text response to speech and print it for logging/screenshot purposes."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    """
    Capture audio from the microphone and convert it to text
    using Google's Speech Recognition API (via SpeechRecognition library).
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return ""

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable right now. Please check your internet connection.")
        return ""


# 2. FEATURE FUNCTIONS


def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


def tell_date():
    today = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")


def open_application(command):
    """
    Opens common applications/websites based on keywords in the command.
    Extend this dictionary with more apps/paths as needed for your OS.
    """
    apps = {
        "notepad": "notepad",          # Windows built-in
        "calculator": "calc",          # Windows built-in
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "gmail": "https://mail.google.com",
    }

    for keyword, target in apps.items():
        if keyword in command:
            speak(f"Opening {keyword}")
            if target.startswith("http"):
                webbrowser.open(target)
            else:
                try:
                    os.system(target)
                except Exception as e:
                    speak(f"Sorry, I could not open {keyword} on this system.")
                    print(f"Error: {e}")
            return True
    return False


def search_wikipedia(command):
    """Search Wikipedia for a query, triggered by phrases like 'who is' or 'what is'."""
    if not WIKIPEDIA_AVAILABLE:
        speak("Wikipedia search is not available. Please install the wikipedia package.")
        return

    query = command.replace("search", "").replace("who is", "") \
                    .replace("what is", "").replace("tell me about", "").strip()

    if not query:
        speak("What would you like me to search for?")
        return

    speak(f"Searching Wikipedia for {query}")
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("That query is too broad. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I could not find any results for that.")
    except Exception as e:
        speak("Something went wrong while searching Wikipedia.")
        print(f"Error: {e}")


def open_website(command):
    """Fallback: open a plain website if the user says 'open <site>'."""
    site = command.replace("open", "").strip()
    if site:
        speak(f"Opening {site}")
        webbrowser.open(f"https://www.{site}.com")
        return True
    return False


# 3. COMMAND PROCESSING (core logic)

def process_command(command):
    """
    Match the recognized text against supported command patterns
    and call the matching feature function. Returns False to signal
    the assistant should stop listening (exit command).
    """
    if not command:
        return True

    if "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "open" in command and open_application(command):
        pass  # handled inside open_application

    elif command.startswith("open") or "open" in command:
        open_website(command)

    elif "who is" in command or "what is" in command or "search" in command:
        search_wikipedia(command)

    elif "hello" in command or "hi" in command:
        speak("Hello! How can I help you today?")

    elif "your name" in command:
        speak("I am your AI voice assistant, built for the major project.")

    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye! Shutting down the assistant.")
        return False

    else:
        speak("I did not understand that command. Please try again.")

    return True



# 4. MAIN PROGRAM LOOP

def main():
    speak("Hello, I am your voice assistant. How can I help you?")

    running = True
    while running:
        command = listen()
        running = process_command(command)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAssistant stopped by user.")
        sys.exit(0)
