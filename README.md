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

## Troubleshooting

### Desktop version
- **"Could not understand audio"** → speak clearly, reduce background
  noise, make sure your microphone is set as the default recording device.
- **`pyttsx3` gives no sound on Linux** → install `espeak`
  (`sudo apt-get install espeak`).
- **No internet** → Speech-to-text (Google Speech API) and Wikipedia search
  need an internet connection; time/date and opening local apps work
  offline.
- No mic/speakers? Choose **Text Mode (2)** from the menu instead.

### Web version — microphone not working
If clicking the mic listens for a second and then goes idle without
picking up your voice, it's almost always a **browser or OS permission**
issue, not a bug in the code. Work through these in order:

**1. Confirm you're on the right address**
The page must be opened at `http://127.0.0.1:5000` (served by Flask), not
opened as a local file. Voice input only works on `localhost` or HTTPS.

**2. Reset the microphone permission in Chrome**
- Go to `chrome://settings/content/microphone`
- Under **"Not allowed to use your microphone,"** remove `127.0.0.1:5000`
  if it's listed
- Refresh the page and click the mic — Chrome should prompt **Allow**

**3. Check your operating system's microphone permissions**
- **Windows**: Settings → Privacy & security → Microphone → turn on
  "Microphone access" and make sure Chrome is allowed
- **Mac**: System Settings → Privacy & Security → Microphone → enable
  Google Chrome (quit and reopen Chrome if it's not listed yet)

**4. Check the correct microphone is selected as input device**
- **Windows**: right-click the speaker icon → Sound settings → Input →
  confirm the right mic is selected and its level bar moves when you speak
- **Mac**: System Settings → Sound → Input → same check

**5. Speak immediately after clicking the mic**
Some browsers start a short silence timeout right away — don't pause
before talking.

**6. Check the browser console for the exact error**
Press **F12** → **Console** tab, click the mic, and read any red error
text — it will say exactly what failed (e.g. permission denied, no
speech detected, no microphone found).

Once permission is granted correctly, do a full page refresh (not just
another click) before testing the mic again.

---

