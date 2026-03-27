import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate variabel waktu (t)
t = np.linspace(0, 1, 1000)

# Step 2: Mendefinisikan parameter dasar sinyal
A = 3  # Amplitudo
f = 3  # Frekuensi

# Menghasilkan sudut fase (ph) acak dengan distribusi uniform rentang -1 hingga +1
# Fungsi np.random.uniform akan mengembalikan nilai acak di antara batas tersebut
ph = np.random.uniform(-1, 1)

# Step 3: Generate sinyal sinus dengan fase acak tersebut
# Sesuai dengan persamaan dasar x(t) = A sin(2πft + Φ)
x = A * np.sin(2 * np.pi * f * t + ph)

# Step 4: Plotting sinyal
plt.plot(t, x, label=f'Fase (Φ) acak = {ph:.4f}')

# Menambahkan keterangan pada grafik
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sinyal Sinusoidal dengan Fase Acak (Uniform -1 s.d 1)')
plt.legend()
plt.show()