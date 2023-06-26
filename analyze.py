import librosa
import librosa.display
import matplotlib.pyplot as plt
import platform
import numpy as np 
import math

audio_data = 'record/filename.wav'

data, sampling_rate = librosa.load(audio_data)
plt.figure(figsize=(12, 4))

if platform.system() == "Darwin":
    librosa.display.waveshow(data, sr=sampling_rate)
else:
    librosa.display.waveplot(data, sr=sampling_rate)


data_length = len(data) 
nfft_half = math.trunc(data_length/2)
k = np.arange(data_length) 
f = k*1000/data_length

nfft_half = math.trunc(data_length/2)
func_half = f[range(nfft_half)] 

fft = np.fft.fft(data)/data_length * 2 
fft_result = fft[range(nfft_half)]


plt.figure()  
plt.plot(func_half, abs(fft_result))
plt.show()