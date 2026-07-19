# AI-Based Voice Assistant

A basic Python voice assistant that listens to voice commands, converts
speech to text, performs an action, and replies back using speech.

## Files in this folder
- `voice_assistant.py` — main project code
- `requirements.txt` — Python packages needed
- `README.md` — this file (setup + run instructions)

## Features
- Tell the current time / date
- Open apps (Notepad, Calculator) or websites (Google, YouTube)
- Search Wikipedia for a topic
- Basic greetings / conversation ("hello", "your name", "thanks")
- Say "exit", "stop", "quit" or "bye" to close the assistant
- **Text Mode fallback**: if you don't have a microphone or speakers handy
  (e.g. testing on a lab PC), you can type commands instead of speaking them —
  useful for testing and for taking screenshots.

---

## How to Run

### 1. Install Python
Make sure Python 3.9+ is installed. Check with:
```
python --version
```

### 2. Install the required packages
Open a terminal/command prompt **inside this project folder** and run:

```
pip install -r requirements.txt
```

**Important — PyAudio (needed for microphone input):**

- **Windows:**
  ```
  pip install pipwin
  pipwin install pyaudio
  ```
  (If that fails, download the matching PyAudio `.whl` file from
  https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio and install it with
  `pip install <file>.whl`)

### 3. Run the program
```
python voice_assistant.py
```

You will see a menu:
```
1. Voice Mode (use microphone)
2. Text Mode  (type commands, no microphone needed)
```

- Choose **1** to speak your commands into the microphone.
- Choose **2** to type commands instead (handy if a microphone isn't
  available, or for quick testing / screenshots).

### 4. Example commands to try
- "What time is it"
- "What is today's date"
- "Open notepad" / "Open calculator" / "Open google" / "Open youtube"
- "Who is Albert Einstein" / "Search Wikipedia for Python programming"
- "Hello" / "What is your name" / "Thank you"
- "Exit" (to quit)

---



