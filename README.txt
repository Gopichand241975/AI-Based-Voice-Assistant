AI-Based Voice Assistant - Major Project

Files:
- voice_assistant.py  -> Original voice (microphone + speaker) version
- app.py              -> NEW: Web interface version (type a command, see the reply)
- templates/index.html -> Chat-style front end used by app.py


*Web Interface (app.py) 

No microphone needed. Type a command in a browser and get an instant
reply on screen. Great for demos, screenshots, and grading.

1. Install Python 3.8+
2. Install dependencies:
   pip install flask wikipedia
3. Run the program:
   python app.py
4. Open your browser at:
   http://127.0.0.1:5000
5. Type commands into the input box, e.g.:
   - "what is the time"
   - "what is the date"
   - "open google"
   - "who is Albert Einstein"
   - "your name: voice assitant"
   You can also just click the quick-suggestion chips under the chat box.


Notes:
- Both versions share the same command logic (time, date, open app/site,
  Wikipedia search, greetings, exit).
- voice_assistant.py requires an internet connection (Google Speech
  Recognition API and Wikipedia) and a working microphone/speakers.
- app.py only needs an internet connection for Wikipedia search; it works
  on any machine since it uses a web page instead of a microphone.
- pyaudio installation (for voice_assistant.py) varies by OS - see comments
  at top of voice_assistant.py.
