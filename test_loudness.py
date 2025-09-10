# test SHM loudness
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from mosqito.utils import load
from src.py.metrics.ecma418_2 import acousticSHMLoudness

# Add the src/py directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Define path to the .wav file
# To be replaced by your own path
path = r"D:\Documents\GitHub\refmap-psychoacoustics\res\JPEL_WM\Broad_conv"
# load signal
loudness = {}
for file in os.listdir(path):
    if file.endswith(".wav"):
        file_path = os.path.join(path, file)
        sr, audio_data = wavfile.read(file_path)
        print(f"Loaded {file} with sample rate {sr} Hz")
        # compute loudness
        loudness[file] = acousticSHMLoudness(audio_data, sr)
# alternatively use mosqito load function
#def acousticSHMLoudness(p, sampleRateIn, axisN=0, soundField='freeFrontal', waitBar=True, outPlot=False, binaural=True)
# save results
import pandas as pd
df = pd.DataFrame.from_dict(loudness, orient='index')
df.to_csv('loudness_SHM_results.csv')