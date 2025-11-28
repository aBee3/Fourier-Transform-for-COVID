import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt


def load_signal_from_csv(folder, index):
    """Load a CSV audio file by 1-based index."""
    files = sorted([f for f in os.listdir(folder) if f.endswith(".csv")])
    file_path = os.path.join(folder, files[index])
    signal = np.loadtxt(file_path, delimiter=",")
    return signal, files[index]


def plot_selected_spectrograms(healthy_folder, covid_folder, output="compare.png", sample_rate=44100):
    # Select the indices
    healthy_indices = [1, 2, 3]
    covid_indices = [2, 3, 4]

    plt.figure(figsize=(15, 8))
    plt.suptitle("Saludable vs COVID - Muestras aleatorias", fontsize=18)

    # Plot Healthy (top row)
    for i, idx in enumerate(healthy_indices, start=1):
        signal, name = load_signal_from_csv(healthy_folder, idx)
        S = librosa.stft(signal)
        S_db = librosa.amplitude_to_db(abs(S))

        ax = plt.subplot(2, 3, i)
        librosa.display.specshow(S_db, sr=sample_rate, x_axis="time", y_axis="hz", ax=ax)
        ax.set_title(f"Saludable {idx}", fontsize=12)
        ax.set_xticks([])
        ax.set_yticks([])

    # Plot Covid (bottom row)
    for j, idx in enumerate(covid_indices, start=1):
        signal, name = load_signal_from_csv(covid_folder, idx)
        S = librosa.stft(signal)
        S_db = librosa.amplitude_to_db(abs(S))

        ax = plt.subplot(2, 3, 3 + j)
        librosa.display.specshow(S_db, sr=sample_rate, x_axis="time", y_axis="hz", ax=ax)
        ax.set_title(f"Covid {idx}", fontsize=12)
        ax.set_xticks([])
        ax.set_yticks([])

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(output, dpi=160)
    plt.close()

    print(f"Figura guardada en: {output}")


plot_selected_spectrograms(
    healthy_folder="healthyCSV",
    covid_folder="covidCSV",
    output="healthy_vs_covid_selected.png"
)

