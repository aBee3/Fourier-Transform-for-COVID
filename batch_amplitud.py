import os
import numpy as np
import matplotlib.pyplot as plt

def plot_50_signals(csv_folder, label, output_file, sample_rate=44100):
    csv_files = sorted([f for f in os.listdir(csv_folder) if f.endswith(".csv")])[:50]

    plt.figure(figsize=(20, 20))
    plt.suptitle(f"Amplitud: Primeras 50 muestras de {label}", fontsize=20)

    for i, file in enumerate(csv_files):
        file_path = os.path.join(csv_folder, file)
        
        # Load CSV audio
        signal = np.loadtxt(file_path, delimiter=",")
        
        # Create time axis
        time = np.arange(len(signal)) / sample_rate
        
        # Plot each of 50 signals
        ax = plt.subplot(10, 5, i + 1)
        ax.plot(time, signal)
        ax.set_title(f"{label} {i+1}", fontsize=8)
        ax.set_xticks([])
        ax.set_yticks([])

    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.savefig(output_file, dpi=150)
    plt.close()

    print(f"Saved figure: {output_file}")

plot_50_signals("healthyCSV", "healthy", "plots_comparativos/first_50_healthy_amplitud.png")
plot_50_signals("covidCSV", "covid", "plots_comparativos/first_50_covid_amplitud.png")