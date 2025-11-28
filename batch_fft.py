import os
import numpy as np
import matplotlib.pyplot as plt

def plot_50_fft(csv_folder, label, output_file, sample_rate=44100):
    csv_files = sorted([f for f in os.listdir(csv_folder) if f.endswith(".csv")])[:50]

    plt.figure(figsize=(20, 20))
    plt.suptitle(f"Primeras 50 Transformadas de Fourier de {label}", fontsize=20)

    for i, file in enumerate(csv_files):
        file_path = os.path.join(csv_folder, file)
        
        # Load CSV audio
        signal = np.loadtxt(file_path, delimiter=",")
        
        # FFT
        fft_data = np.fft.fft(signal)
        freqs = np.fft.fftfreq(len(signal), 1 / sample_rate)

        # Keep only positive frequencies
        pos_freqs = freqs[:len(freqs)//2]
        magnitude = np.abs(fft_data[:len(freqs)//2])
        
        # Plot each FFT
        ax = plt.subplot(10, 5, i + 1)
        ax.plot(pos_freqs, magnitude)
        ax.set_title(f"{label} {i+1}", fontsize=8)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(0, np.max(pos_freqs))

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"Saved figure: {output_file}")


plot_50_fft("healthyCSV", "healthy", "plots_comparativos/first_50_healthy_fft.png")
plot_50_fft("covidCSV", "covid", "plots_comparativos/first_50_covid_fft.png")