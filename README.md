# AI-Based Voice Assistant — Major Project (Option A)

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
  (`espeak` is required so `pyttsx3` can actually speak on Linux.)

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

## Troubleshooting
- **"Could not understand audio"** → speak clearly, reduce background noise,
  and make sure your microphone is set as the default recording device.
- **`pyttsx3` gives no sound on Linux** → install `espeak`
  (`sudo apt-get install espeak`).
- **No internet** → Speech-to-text (Google Speech API) and Wikipedia search
  both need an active internet connection; time/date and opening local apps
  work fully offline.
- If the microphone or speakers are not available at all, simply choose
  **Text Mode (2)** from the menu — all other logic and features work the
  same way, just using keyboard input instead of the microphone.

---

## For Your Project Submission
1. Take a screenshot of the program running (menu + a command + response).
2. Take screenshots of at least 2–3 different features being demonstrated
   (e.g. time, opening an app, Wikipedia search).
3. Place all screenshots in a folder named: `MajorProject_YourName`
4. Prepare your documentation PDF named: `MajorProject_YourName.pdf`,
   including: Project Title, Problem Statement, Objective, Tools &
   Technologies, System Architecture/Model Description, Code Explanation,
   Screenshots, Results, Conclusion, and Future Scope.
5. Submit everything through the Google Form as instructed (do not use email
   or any other platform).
