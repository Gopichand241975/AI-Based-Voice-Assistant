"""
AI-Based Voice Assistant:

A basic voice assistant that can:
    1. Listen to voice commands (Speech to Text)
    2. Process the command
    3. Perform an action (tell time, open apps, search Wikipedia, etc.)
    4. Respond back using speech (Text to Speech)

"""

import datetime
import os
import sys
import webbrowser
import aifc

import speech_recognition as sr
import pyttsx3

try:
    import wikipedia
    WIKIPEDIA_AVAILABLE = True
except ImportError:
    WIKIPEDIA_AVAILABLE = False



# Text to Speech Engine Setup

try:
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)      # speaking speed
    engine.setProperty("volume", 1.0)    # volume level (0.0 to 1.0)
    TTS_AVAILABLE = True
except Exception:
    # No audio driver found (e.g. eSpeak missing on Linux). The assistant
    # will still work in text-only mode so the project never crashes.
    engine = None
    TTS_AVAILABLE = False


def speak(text):
    """Convert text response to speech and print it on screen too."""
    print(f"Assistant: {text}")
    if TTS_AVAILABLE:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass



# Speech to Text (Listening)

def listen_command():
    """
    Capture audio from the microphone and convert it to text.
    Returns the recognized command in lowercase, or an empty string on failure.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening... Please speak your command.")
        recognizer.adjust_for_ambient_noise(source, duration=0.8)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            speak("I did not hear anything. Please try again.")
            return ""

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable. Check your internet connection.")
        return ""



# Actions / Features

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


def tell_date():
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    speak(f"Today's date is {today}")


def open_application(command):
    """Open common applications based on the platform (Windows / Linux / Mac)."""
    apps = {
        "notepad": {"win32": "notepad.exe", "linux": "gedit", "darwin": "TextEdit"},
        "calculator": {"win32": "calc.exe", "linux": "gnome-calculator", "darwin": "Calculator"},
        "browser": {"win32": "start chrome", "linux": "xdg-open http://google.com",
                    "darwin": "open -a Safari"},
    }

    for app_name, platform_cmds in apps.items():
        if app_name in command:
            cmd = platform_cmds.get(sys.platform.rstrip("0123456789"), None)
            if sys.platform.startswith("win"):
                cmd = platform_cmds["win32"]
            elif sys.platform.startswith("linux"):
                cmd = platform_cmds["linux"]
            elif sys.platform.startswith("darwin"):
                cmd = platform_cmds["darwin"]

            speak(f"Opening {app_name}")
            try:
                os.system(cmd)
            except Exception as e:
                speak(f"Sorry, I could not open {app_name}. Error: {e}")
            return True
    return False


def search_wikipedia(command):
    """Search Wikipedia for a topic mentioned after the word 'search' or 'who is' / 'what is'."""
    if not WIKIPEDIA_AVAILABLE:
        speak("Wikipedia feature is not available. Please install the wikipedia package.")
        return

    query = command
    for keyword in ["search wikipedia for", "search for", "who is", "what is", "search"]:
        query = query.replace(keyword, "")
    query = query.strip()

    if not query:
        speak("Please tell me what you want to search.")
        return

    try:
        speak(f"Searching Wikipedia for {query}")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results for that. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I could not find anything on that topic.")
    except Exception:
        speak("Something went wrong while searching Wikipedia.")


def open_website(command):
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "wikipedia": "https://www.wikipedia.org",
    }
    for name, url in sites.items():
        if name in command:
            speak(f"Opening {name}")
            webbrowser.open(url)
            return True
    return False


def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning! I am your voice assistant. How can I help you?")
    elif hour < 18:
        speak("Good afternoon! I am your voice assistant. How can I help you?")
    else:
        speak("Good evening! I am your voice assistant. How can I help you?")



# Command Processing (Main Logic)

def process_command(command):
    """
    Match the recognized command text against known keywords
    and trigger the corresponding action. Returns False if the
    user asked to exit, True otherwise.
    """
    if not command:
        return True

    if "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "open" in command:
        if not open_website(command):
            if not open_application(command):
                speak("Sorry, I don't know that application.")

    elif "search" in command or "who is" in command or "what is" in command:
        search_wikipedia(command)

    elif "hello" in command or "hi" in command:
        speak("Hello! How can I assist you today?")

    elif "your name" in command:
        speak("I am your personal AI voice assistant, built in Python.")

    elif "thank you" in command or "thanks" in command:
        speak("You are welcome!")

    elif "exit" in command or "stop" in command or "quit" in command or "bye" in command:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        speak("Sorry, I did not understand that command. Please try again.")

    return True



# Text-Mode Fallback (useful when no microphone is available / for testing)

def run_text_mode():
    speak("Running in text mode. Type your commands below.")
    greet_user()
    running = True
    while running:
        command = input("\nType your command (or 'exit' to quit): ").lower().strip()
        running = process_command(command)



# Voice-Mode Main Loop

def run_voice_mode():
    greet_user()
    running = True
    while running:
        command = listen_command()
        running = process_command(command)



# Entry Point

if __name__ == "__main__":
    print("=" * 55)
    print("        AI-BASED VOICE ASSISTANT - MAJOR PROJECT")
    print("=" * 55)
    print("1. Voice Mode (use microphone)")
    print("2. Text Mode  (type commands, no microphone needed)")
    print("=" * 55)

    choice = input("Choose mode (1/2): ").strip()

    if choice == "1":
        try:
            run_voice_mode()
        except Exception as e:
            print(f"Voice mode failed ({e}). Switching to text mode...")
            run_text_mode()
    else:
        run_text_mode()
