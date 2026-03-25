import speech_recognition as sr
import webbrowser
import pyttsx3
import time
from musiclib import music
from nova_ollama import ask_nova

r = sr.Recognizer()

# Initialize engine ONCE
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)


#  FIXED speak function (NO FREEZE)
def speak(text):
    print("Nova:", text)
    try:
        engine.stop()   # 🔥 important fix
    except:
        pass

    engine.say(text)
    engine.runAndWait()
    time.sleep(0.2)  # 🔥 small delay to avoid audio clash


def processCommand(c):
    c = c.lower()

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open instagram" in c:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open github" in c:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif c.startswith("play"):
        song = c.replace("play", "").strip().lower()

        if song in music:
            speak(f"Playing {song}")
            webbrowser.open(music[song])
        else:
            speak(f"Playing {song} on YouTube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

    else:
        speak("Let me think...")
        reply = ask_nova(c)
        print("AI:", reply)
        speak(reply)


if __name__ == "__main__":
    speak("Initializing Nova")
    speak("Say Nova to activate me")

    while True:
        print("\nWaiting for wake word 'Nova'...")

        try:
            # 🎤 Wake word listening
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=5, phrase_time_limit=3)

            try:
                word = r.recognize_google(audio)
                print("Detected:", word)

                if "nova" in word.lower():
                    speak("Yes Garv")

                    time.sleep(0.5)  # 🔥 mic & speaker sync

                    # 🎤 Command listening
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        r.adjust_for_ambient_noise(source, duration=0.5)
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)

                    try:
                        command = r.recognize_google(audio)
                        print("Command:", command)

                        processCommand(command)

                    except sr.UnknownValueError:
                        speak("Sorry, I did not understand")

                    except sr.RequestError:
                        speak("Internet issue")

            except sr.UnknownValueError:
                pass

            except sr.RequestError:
                speak("Network error")

        except Exception as e:
            print("Error:", e)


            