
# This code processes de Fast Fourier Transform to all the audio files in the project.
# It then creates a spectogram of each, and saves them in the folder.
# Files have already been uploaded, there's no need for this code to be re-run.

import os
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

def process_folder(csv_folder, label, output_folder, start_index=1, sample_rate=44100):
    os.makedirs(output_folder, exist_ok=True)

    csv_files = sorted([f for f in os.listdir(csv_folder) if f.endswith(".csv")])

    for i, file in enumerate(csv_files, start=start_index):
        file_path = os.path.join(csv_folder, file)

        # Load the CSV audio
        signal = np.loadtxt(file_path, delimiter=",")

        # ------------------------------------
        # 1. FFT
        # ------------------------------------
        fft_data = np.fft.fft(signal)
        freqs = np.fft.fftfreq(len(signal), 1 / sample_rate)

        # ------------------------------------
        # 2. Spectrogram using STFT
        # ------------------------------------
        S = librosa.stft(signal)
        S_db = librosa.amplitude_to_db(abs(S))

        # ------------------------------------
        # 3. Plot spectrogram
        # ------------------------------------
        plt.figure(figsize=(8, 4))
        librosa.display.specshow(S_db, sr=sample_rate, x_axis='time', y_axis='hz')
        plt.colorbar(format="%+2.f dB")
        plt.title(f"{label} {i}")
        
        # Save image
        output_path = os.path.join(output_folder, f"{label}_{i}.png")
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()

        print(f"Saved: {output_path}")


# ------------------------------------
# EXAMPLE USAGE
# ------------------------------------

# Folder structure example:
# data/
#   healthy_csv/
#   covid_csv/

process_folder(
    csv_folder="healthyCSV",
    label="healthy",
    output_folder="plot_healthy"
)

process_folder(
    csv_folder="covidCSV",
    label="covid",
    output_folder="plot_covid"
)
