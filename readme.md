Nova : Nova is a Python-based voice assistant that can listen to your voice, process commands, and respond intelligently using AI.
Features: 
🎤 Voice input using SpeechRecognition
🔊 Text-to-Speech response
🤖 AI-powered responses (Gemini API)
⚡ FastAPI backend support
🌐 CORS enabled for frontend integration

Tech Stack
Python 3.11 #cause pyaudio is not available in latest version
FastAPI
SpeechRecognition
PyAudio
Google Generative AI (Gemini)
Uvicorn

Project Structure
Nova/
│── main.py
│── requirements.txt
│── .env
│── README.md

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone <your-repo-link>
cd Nova
2️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add Environment Variables

Create a .env file and add:

GEMINI_API_KEY=your_api_key_here

5️⃣ Run the Project
python main.py

🎯 Usage
Run the script
Speak into your microphone
Nova will listen and respond
🧠 Challenges Faced
PyAudio installation issues on Python 3.13
Resolved by using Python 3.11 and virtual environments
📌 Future Improvements
GUI integration
Better command recognition
Multi-language support
Deployment on cloud
👨‍💻 Author

Garv Manchal

⭐ Acknowledgements
Python community
OpenAI / Google AI
SpeechRecognition library

import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio
import time

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    

if __name__ == "__main__" :
    speak(" Initializing Nova......")
    
    while True :
        # listen for the wake word Nova
        print("Recognizing....")

        try:
            with sr.Microphone() as source:
                print("Nova is listening...")
                audio = r.listen( source,timeout=5,phrase_time_limit=2)

            word = r.recognize_google(audio)
            print("Detected Word: ",word)


            if (word.lower() == "nova"):
                print("wake word detected")
                speak("Hii Grvv")
                time.sleep(1)

                #Listen for command
                with sr.Microphone() as source:
                    print("Nova Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
                    print(command)
           
                    

                    

        except Exception as e :
            print("error; {0}".format(e))

