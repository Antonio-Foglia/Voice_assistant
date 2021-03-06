import googletrans as gt
from googletrans import Translator
from __output__ import say
#from __ML__ import tml

def translate(text):
    li=text.lower().split(' ')
    #tml(li)
    try:
        pos1=li.index('translate')
    except:
        pos1=li.index('say')
    text=' '.join(li[pos1+1:-2])
    lang=li[-1]
    if lang == 'chinese':
        lang='chinese (simplified)'
    code=gt.LANGCODES[lang]
    translator = Translator()
    final=translator.translate(text ,scr='en', dest=code)
    say('{} in {} is:'.format(text,lang),'en')
    try:
        say(final.text,final.dest)
    except:
        say(final.text,'en')
    return
