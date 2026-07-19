
import datetime
import webbrowser as wb

from flask import Flask, request, jsonify, render_template

try:
    import wikipedia
    WIKIPEDIA_AVAILABLE = True
except ImportError:
    WIKIPEDIA_AVAILABLE = False

app = Flask(__name__)



# FEATURE FUNCTIONS
# Each function returns a text reply (instead of speaking it out loud).

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {current_time}."


def tell_date():
    today = datetime.datetime.now().strftime("%B %d, %Y")
    return f"Today's date is {today}."


APPS = {
    "notepad": "notepad",
    "calculator": "calc",
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com",
}


def open_application(command):
    """Return a reply for 'open <app/site>' style commands, and open it
    in a browser tab when it is a website (works from the local machine
    running this server)."""
    for keyword, target in APPS.items():
        if keyword in command:
            if target.startswith("http"):
                try:
                    wb.open(target)
                except Exception:
                    pass
                return f"Opening {keyword} -> {target}"
            return f"Opening {keyword} (desktop apps can only be launched on the local machine running this server)."
    return None


def open_website(command):
    site = command.replace("open", "").strip()
    if site:
        url = f"https://www.{site}.com"
        try:
            wb.open(url)
        except Exception:
            pass
        return f"Opening {url}"
    return None


def search_wikipedia(command):
    if not WIKIPEDIA_AVAILABLE:
        return "Wikipedia search is not available. Please install the 'wikipedia' package."

    query = command.replace("search", "").replace("who is", "") \
                    .replace("what is", "").replace("tell me about", "").strip()

    if not query:
        return "What would you like me to search for?"

    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError:
        return "That query is too broad. Please be more specific."
    except wikipedia.exceptions.PageError:
        return "Sorry, I could not find any results for that."
    except Exception:
        return "Something went wrong while searching Wikipedia."


# COMMAND PROCESSING (core logic -- same rules as voice_assistant.py)


def process_command(raw_command):
    command = (raw_command or "").strip().lower()

    if not command:
        return "I didn't catch that. Please type a command."

    if "time" in command:
        return tell_time()

    if "date" in command:
        return tell_date()

    if "open" in command:
        reply = open_application(command)
        if reply:
            return reply
        reply = open_website(command)
        if reply:
            return reply
        return "Please tell me what to open, e.g. 'open google'."

    if "who is" in command or "what is" in command or "search" in command:
        return search_wikipedia(command)

    if "hello" in command or "hi" in command:
        return "Hello! How can I help you today?"

    if "your name" in command:
        return "I am your AI voice assistant, built for the major project."

    if "exit" in command or "quit" in command or "stop" in command:
        return "Goodbye! (You can keep chatting anytime - just type a new command.)"

    return "I did not understand that command. Try 'time', 'date', 'open google', or 'who is Albert Einstein'."


# ROUTES

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/command", methods=["POST"])
def api_command():
    data = request.get_json(silent=True) or {}
    user_text = data.get("command", "")
    reply = process_command(user_text)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
