import librosa
import librosa.display
import matplotlib.pyplot as plt

audio_data = 'record/filename.wav'

data, sampling_rate = librosa.load(audio_data)
plt.figure(figsize=(12, 4))

librosa.display.waveplot(data, sr=sampling_rate)
plt.show()

print(data)