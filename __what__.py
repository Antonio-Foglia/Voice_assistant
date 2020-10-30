from __translate__ import translate
from __weather__ import weather
from __chat__ import chat
from __seriea__ import serie_a

def what_is(text):
    if 'translate' in text or 'say' in text and 'in' in text:
        translate(text)
        return 
    elif 'weather' in text:
        weather(text)
        return  
    elif 'shut up' in text or 'turn off' in text:
        return 'quit'
    elif 'ac' in text and 'milan' in text or 'serie' in text and 'a' in text:
        serie_a(text)
        return
    else:
        chat(text)
        return
