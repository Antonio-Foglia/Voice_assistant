from __input__ import inp
from __recognise__ import recognise
from __what__ import what_is
import time
from playsound import playsound
from __face_rec__ import fr
import os


def main():
    fr()
    playsound('sounds/intro.mp3')
    input('Press enter to ask something')
    again = ""
    while again == "":
        fname=inp(6,'input')
        text = recognise(fname).lower()
        print('\nUser: "'+text+'"')
        if 'new' in text and 'user' in text:
            main()
        try:
            if what_is(text) == 'quit':
                    again='not'
        except:
            playsound('sounds/sorry.mp3')
        if again=='':
            time.sleep(1)
            playsound('sounds/again.mp3')
            again=input('Press enter to ask something else')
    print('Turning off...')
    os.remove("pic.jpg")

    return playsound('sounds/off.mp3.mov')

if __name__ == "__main__":
    main()
