import socket
import win32com.client as wc
import msvcrt as m
speak = wc.Dispatch("Sapi.SpVoice")
speak.Speak("The IP IS : ")
speak.Speak(socket.gethostbyname(socket.gethostname()).split())
speak.Speak("And I repeat")
speak.Speak(socket.gethostbyname(socket.gethostname()))
speak.Speak("Thank you for using SpeakIP")
def wait():
    m.getch()
wait()
