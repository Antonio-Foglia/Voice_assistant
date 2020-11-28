import sounddevice as sd
import scipy.io.wavfile as wav
from playsound import playsound


def inp(duration,fname):
    fs=44100
    playsound('sounds/Ping1.mp3.mov')
    data = sd.rec(duration * fs, samplerate=fs, channels=1,dtype='int32')
    sd.wait()
    playsound('sounds/Ping2.mp3.mov')
    wav.write('{}.wav'.format(fname),fs,data)
    return fname+'.wav'
