from scipy.io import wavfile
import noisereduce
import numpy as np

def reduce_noise(file:str, output_file:str):
    rate, data = wavfile.read(file)
    orig_shape = data.shape
    data = np.reshape(data, (2, -1))
    reduced_noise = noisereduce.reduce_noise(y=data, sr=rate, stationary=True)
    wavfile.write(output_file, rate, reduced_noise.reshape(orig_shape))
