import wave
import pyaudio

CHUNK = 1024

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                input=True,
                frames_per_buffer=CHUNK)

frames = []

for i in range(0, int(44100 / CHUNK * 5)):
    data = stream.read(CHUNK)
    frames.append(data)



stream.close()

wf = wave.open('record/filename.wav', 'wb')
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)
wf.writeframes(b''.join(frames))
p.terminate()