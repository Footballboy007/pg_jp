import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Hi Comp Sci class, what do you want to search for?")
    print("Listening...")
    audio = r.listen(source)
    print("thinking...")


try:
    words = r.recognize_google(audio)
    speak.Speak("ok James, ler's look for " + r.recognition_google(audio) +" on google ")
    wb.open("https://www.google.com/search?q=" + words)

except sr.UnknownValueError:
    print("Google speech recognition could not understand audio")
except sr.RequuestError as e:
    print("Could not request results from google speech recognition service; (0)" .format(e))
