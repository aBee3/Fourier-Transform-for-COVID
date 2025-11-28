import os
import numpy as np
import matplotlib.pyplot as plt


def load_signal_from_csv(folder, index):
    """Load a CSV audio file by 1-based index."""
    files = sorted([f for f in os.listdir(folder) if f.endswith(".csv")])
    file_path = os.path.join(folder, files[index - 1])
    signal = np.loadtxt(file_path, delimiter=",")
    return signal, files[index - 1]


def plot_fft_comparison(healthy_folder, covid_folder, output="fft_comparison.png", sample_rate=44100):
    healthy_indices = [1, 2, 3]
    covid_indices = [2, 3, 4]

    plt.figure(figsize=(16, 8))
    plt.suptitle("Transformada de Fourier: Saludable vs COVID", fontsize=18)

    # -----------------------------
    # TOP ROW — HEALTHY
    # -----------------------------
    for i, idx in enumerate(healthy_indices, start=1):
        signal, name = load_signal_from_csv(healthy_folder, idx)

        # FFT
        fft_data = np.fft.fft(signal)
        freqs = np.fft.fftfreq(len(signal), 1/sample_rate)

        # Only positive frequencies
        pos_freqs = freqs[:len(freqs)//2]
        magnitude = np.abs(fft_data[:len(freqs)//2])

        ax = plt.subplot(2, 3, i)
        ax.plot(pos_freqs, magnitude)
        ax.set_title(f"Saludable {idx}", fontsize=12)
        ax.set_xlabel("Frecuencia (Hz)")
        ax.set_ylabel("Amplitud")
        ax.set_xlim(0, max(pos_freqs))  # Keep entire spectrum visible

    # -----------------------------
    # BOTTOM ROW — COVID
    # -----------------------------
    for j, idx in enumerate(covid_indices, start=1):
        signal, name = load_signal_from_csv(covid_folder, idx)

        # FFT
        fft_data = np.fft.fft(signal)
        freqs = np.fft.fftfreq(len(signal), 1/sample_rate)

        # Only positive frequencies
        pos_freqs = freqs[:len(freqs)//2]
        magnitude = np.abs(fft_data[:len(freqs)//2])

        ax = plt.subplot(2, 3, 3 + j)
        ax.plot(pos_freqs, magnitude)
        ax.set_title(f"Covid {idx}", fontsize=12)
        ax.set_xlabel("Frequency (Hz)")
        ax.set_ylabel("Amplitude")
        ax.set_xlim(0, max(pos_freqs))

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(output, dpi=160)
    plt.close()

    print(f"Saved figure: {output}")

plot_fft_comparison(
    healthy_folder="healthyCSV",
    covid_folder="covidCSV",
    output="healthy_vs_covid_fft.png"
)
