# AI-Based Voice Assistant — Major Project
![Voice feature demonstration](Screenshots/voice%20-%20feature%20demonstration.png)

A Python voice assistant that listens to voice commands, converts speech to
text, performs an action, and replies back using speech. This project
includes **two versions**:

1. **Desktop version** (`voice_assistant.py`) — runs in the terminal, uses
   your system microphone directly.
2. **Web version** (`app.py` + `templates/index.html`) — runs in the
   browser, with a mic button, live transcript, and a clear IN/OUT
   conversation log. Great for demos and screenshots.

---

## Files in this project

```
VoiceAssistant/
├── voice_assistant.py       # Desktop version (terminal + microphone)
├── app.py                   # Web version (Flask server)
├── templates/
│   └── index.html           # Web version front end
├── requirements.txt          # Python packages needed
└── README.md                 # this file
```

---

## Features

- Tell the current time / date
- Open apps (Notepad, Calculator) or websites (Google, YouTube)
- Search Wikipedia for a topic
- Basic greetings / conversation ("hello", "your name", "thanks")
- Say "exit", "stop", "quit" or "bye" to close the assistant (desktop version)
- **Text Mode fallback** (desktop version): if you don't have a microphone,
  type commands instead
- **Web version**: mic button + typed input, spoken replies, and a visible
  IN/OUT conversation log — no PyAudio setup required

---

## Option A — Run the Desktop Version

### 1. Install Python
Make sure Python 3.9+ is installed. Check with:
```
python --version
```

### 2. Install the required packages
```
pip install -r requirements.txt
```

**PyAudio (needed for microphone input):**

- **Windows:**
  ```
  pip install pipwin
  pipwin install pyaudio
  ```
  If that fails, download the matching PyAudio `.whl` from
  https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio and install with
  `pip install <file>.whl`

- **macOS:**
  ```
  brew install portaudio
  pip install pyaudio
  ```

- **Linux (Ubuntu/Debian):**
  ```
  sudo apt-get install portaudio19-dev python3-pyaudio espeak
  pip install pyaudio
  ```
  (`espeak` lets `pyttsx3` actually speak on Linux.)

### 3. Run it
```
python voice_assistant.py
```
Choose **1** for Voice Mode (microphone) or **2** for Text Mode (typing).

---

## Option B — Run the Web Version

### 1. Install the required packages
```
pip install -r requirements.txt
```
(No PyAudio needed — the browser handles the microphone.)

### 2. Run the Flask server
Open a terminal **inside this project folder** (the one containing `app.py`)
and run:
```
python app.py
```
You should see:
```
* Running on http://127.0.0.1:5000
```

### 3. Open it in your browser
Go to **http://127.0.0.1:5000** in **Google Chrome** (best support for
in-browser speech recognition).

Important: open the URL above — do **not** double-click `index.html`
directly. The page only works when served by Flask.

### 4. Using it
- Click the mic button and speak, **or** type a command and click Send
- Every exchange is logged: **IN** = what you said/typed, **OUT** = the
  assistant's reply (also spoken aloud)

---

## Example commands to try
- "What time is it"
- "What is today's date"
- "Open notepad" / "Open calculator" / "Open google" / "Open youtube"
- "Who is Albert Einstein" / "Search Wikipedia for Python programming"
- "Hello" / "What is your name" / "Thank you"
- "Exit" (desktop version only)

---

