import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate variabel waktu (t)
t = np.linspace(0, 1, 1000)

# Step 2: Mendefinisikan parameter amplitudo dan fase
A = 3  # Amplitudo tetap
ph = 0 # Fase tetap

# Menghasilkan frekuensi (f) acak dengan distribusi uniform rentang -1 hingga +1
# Fungsi np.random.uniform akan mengembalikan nilai acak di antara batas tersebut
f = np.random.uniform(-1, 1)

# Step 3: Generate sinyal sinus dengan frekuensi acak tersebut
x = A * np.sin(2 * np.pi * f * t + ph)

# Step 4: Plotting sinyal
plt.plot(t, x, label=f'Frekuensi (f) acak = {f:.4f} Hz')

# Menambahkan keterangan pada grafik
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sinyal Sinusoidal dengan Frekuensi Acak (Uniform -1 s.d 1)')
plt.legend()
plt.show()