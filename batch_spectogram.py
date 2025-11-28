import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt


def plot_50_spectrograms(csv_folder, label, output_file, sample_rate=44100):
    csv_files = sorted([f for f in os.listdir(csv_folder) if f.endswith(".csv")])[:50]

    plt.figure(figsize=(20, 20))
    plt.suptitle(f"First 50 {label}", fontsize=20)

    for i, file in enumerate(csv_files):
        file_path = os.path.join(csv_folder, file)
        
        # Load CSV audio
        signal = np.loadtxt(file_path, delimiter=",")
        
        # STFT for spectrogram
        S = librosa.stft(signal)
        S_db = librosa.amplitude_to_db(abs(S))
        
        # Plot each of 50 spectrograms
        ax = plt.subplot(10, 5, i + 1)
        librosa.display.specshow(S_db, sr=sample_rate, x_axis='time', y_axis='hz', ax=ax)
        ax.set_title(f"{label} {i+1}", fontsize=8)
        ax.set_xticks([])
        ax.set_yticks([])

    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"Saved figure: {output_file}")

plot_50_spectrograms("healthyCSV", "healthy", "plot_healthy/first_50_healthy.png")
plot_50_spectrograms("covidCSV", "covid", "plot_covid/first_50_covid.png")