import sounddevice
from scipy.io.wavfile import write

def voice_recoder(seconds,file):
    print("recording started...")
    recording=sounddevice.rec((seconds*44100),samplerate=44100,channels=2)
    sounddevice.wait()
    write(file,44100,recording)
    print("Recording finished...")

voice_recoder(10,"record.wav")