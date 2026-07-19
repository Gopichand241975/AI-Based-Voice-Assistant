"""
AI-Based Voice Assistant — Web Front End
=========================================

This Flask app wraps the same assistant "brain" from voice_assistant.py
(time, date, Wikipedia search, opening websites, greetings, etc.) and
exposes it through a simple web page.


Run with:
    pip install flask wikipedia
    python app.py
Then open http://127.0.0.1:5000 in your browser (Chrome recommended,
since it has the best Web Speech API support).
"""

import datetime

from flask import Flask, render_template, request, jsonify

try:
    import wikipedia
    WIKIPEDIA_AVAILABLE = True
except ImportError:
    WIKIPEDIA_AVAILABLE = False

app = Flask(__name__)


WEBSITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "wikipedia": "https://www.wikipedia.org",
}


def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {current_time}", None


def tell_date():
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    return f"Today's date is {today}", None


def open_website(command):
    for name, url in WEBSITES.items():
        if name in command:
            return f"Opening {name}", {"type": "open_url", "url": url}
    return None, None


def search_wikipedia(command):
    if not WIKIPEDIA_AVAILABLE:
        return "Wikipedia feature is not available on the server.", None

    query = command
    for keyword in ["search wikipedia for", "search for", "who is", "what is", "search"]:
        query = query.replace(keyword, "")
    query = query.strip()

    if not query:
        return "Please tell me what you want to search.", None

    try:
        result = wikipedia.summary(query, sentences=2)
        return f"Here's what I found on {query}: {result}", None
    except wikipedia.exceptions.DisambiguationError:
        return "There are multiple results for that. Please be more specific.", None
    except wikipedia.exceptions.PageError:
        return "Sorry, I could not find anything on that topic.", None
    except Exception:
        return "Something went wrong while searching Wikipedia.", None


def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning! I am your voice assistant. How can I help you?"
    elif hour < 18:
        return "Good afternoon! I am your voice assistant. How can I help you?"
    else:
        return "Good evening! I am your voice assistant. How can I help you?"


def process_command(command):
    """
    Same keyword-matching logic as the desktop version, but returns
    (reply_text, action) instead of speaking directly.
    action is either None or a dict like {"type": "open_url", "url": "..."}
    which the browser's JavaScript will act on (e.g. open a new tab).
    """
    command = (command or "").lower().strip()

    if not command:
        return "I didn't catch that. Could you say it again?", None

    if "time" in command:
        return tell_time()

    if "date" in command:
        return tell_date()

    if "open" in command:
        reply, action = open_website(command)
        if reply:
            return reply, action
        return "I can only open websites (like Google or YouTube) from the browser version.", None

    if "search" in command or "who is" in command or "what is" in command:
        return search_wikipedia(command)

    if "hello" in command or "hi" in command:
        return "Hello! How can I assist you today?", None

    if "your name" in command:
        return "I am your personal AI voice assistant, built in Python and Flask.", None

    if "thank you" in command or "thanks" in command:
        return "You are welcome!", None

    if "exit" in command or "stop" in command or "quit" in command or "bye" in command:
        return "Goodbye! Have a nice day.", None

    return "Sorry, I did not understand that command. Please try again.", None



# Routes


@app.route("/")
def index():
    return render_template("index.html", greeting=greet_user())


@app.route("/process", methods=["POST"])
def process():
    data = request.get_json(force=True) or {}
    command = data.get("command", "")
    reply, action = process_command(command)
    return jsonify({"input": command, "reply": reply, "action": action})


if __name__ == "__main__":
    app.run(debug=True)