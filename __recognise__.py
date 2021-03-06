import speech_recognition as sr
import os


def recognise(fname):
    r = sr.Recognizer()
    with sr.AudioFile(fname) as source:
        audio = r.record(source)
    os.remove(fname)
    try:
        th=r.recognize_google(audio)
        #print(f'User: "{th}"')
        return th
    except sr.UnknownValueError:
         return ("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        return ("Could not request results from Google Speech Recognition service")
