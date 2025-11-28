import os
import numpy as np
import matplotlib.pyplot as plt


def load_signal_from_csv(folder, index):
    """Load a CSV audio file by 1-based index."""
    files = sorted([f for f in os.listdir(folder) if f.endswith(".csv")])
    file_path = os.path.join(folder, files[index - 1])
    signal = np.loadtxt(file_path, delimiter=",")
    return signal, files[index - 1]


def plot_amplitude_comparison(healthy_folder, covid_folder, output="amplitude_comparison.png", sample_rate=44100):
    healthy_indices = [1, 2, 3]
    covid_indices = [2, 3, 4]

    plt.figure(figsize=(16, 8))
    plt.suptitle("Comparasión Amplitud de Audio: Saludable vs Covid (Waveform)", fontsize=18)

    # -----------------------------
    # TOP ROW — HEALTHY (time-domain)
    # -----------------------------
    for i, idx in enumerate(healthy_indices, start=1):
        signal, name = load_signal_from_csv(healthy_folder, idx)
        
        # Time axis for plotting
        time = np.arange(len(signal)) / sample_rate

        ax = plt.subplot(2, 3, i)
        ax.plot(time, signal)
        ax.set_title(f"Saludable {idx}", fontsize=12)
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Amplitud")
        ax.set_xlim(0, time[-1])

    # -----------------------------
    # BOTTOM ROW — COVID (time-domain)
    # -----------------------------
    for j, idx in enumerate(covid_indices, start=1):
        signal, name = load_signal_from_csv(covid_folder, idx)

        time = np.arange(len(signal)) / sample_rate

        ax = plt.subplot(2, 3, 3 + j)
        ax.plot(time, signal)
        ax.set_title(f"Covid {idx}", fontsize=12)
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Amplitud")
        ax.set_xlim(0, time[-1])

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(output, dpi=160)
    plt.close()

    print(f"Figura guardada correctamente en: {output}")

plot_amplitude_comparison(
    healthy_folder="healthyCSV",
    covid_folder="covidCSV",
    output="ampltud_saludable_vs_covid.png"
)

