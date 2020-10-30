from gtts import gTTS
import os
from playsound import playsound

def say(text,lang):
    if '[' not in text:
        print(f'Goffredo: "{text}"')
    tts = gTTS(text=text, lang=lang)
    tts.save("x.mp3")
    return playsound('x.mp3'),os.remove('x.mp3')
    