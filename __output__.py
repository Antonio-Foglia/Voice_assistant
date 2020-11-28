from gtts import gTTS
import os
from playsound import playsound
import time

def say(text,lang):
    if '[' not in text:
        print(f'Goffredo: "{text}"')
    tts = gTTS(text=text, lang=lang)
    tts.save("x.mp3")
    time.sleep(1)#vary this based on internet speed
    return playsound('x.mp3'),os.remove('x.mp3')
