# This code ran once, it's not meant to be ran again as the CSV files are already converted.
# If you wish to replicate the comparison with another database, get your files in the folders /covid and /healthy.
# These folders must contain the .wav file
# These folders no longer exist in the repo, you can download the db from: https://github.com/toborobot/CoughDataset

import glob
import os
import numpy as np
from scipy.io import wavfile

input_folder = "covid"
output_folder = "covidCSV"
os.makedirs(output_folder, exist_ok=True)

for wav_path in glob.glob(os.path.join(input_folder, "*.wav")):
    _, data = wavfile.read(wav_path)

    # Convert stereo → mono if needed
    if len(data.shape) == 2:
        data = data.mean(axis=1)

    base = os.path.basename(wav_path).replace(".wav", ".csv")
    csv_path = os.path.join(output_folder, base)

    np.savetxt(csv_path, data, delimiter=",")
    print("Saved:", csv_path)

input_folder = "healthy"
output_folder = "healthyCSV"
os.makedirs(output_folder, exist_ok=True)

for wav_path in glob.glob(os.path.join(input_folder, "*.wav")):
    _, data = wavfile.read(wav_path)

    # Convert stereo → mono if needed
    if len(data.shape) == 2:
        data = data.mean(axis=1)

    base = os.path.basename(wav_path).replace(".wav", ".csv")
    csv_path = os.path.join(output_folder, base)

    np.savetxt(csv_path, data, delimiter=",")
    print("Saved:", csv_path)
    