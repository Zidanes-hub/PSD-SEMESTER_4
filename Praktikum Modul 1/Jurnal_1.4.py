import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate variabel t (waktu)
t = np.linspace(0, 1, 1000)

# Step 2: Mendefinisikan variabel amplitudo, frekuensi, dan fase
A = 3
f = 3
ph = 0

# Step 3: Generate sinyal sinus dan cosinus
# Sinyal sinus sesuai persamaan dasar
x_sinus = A * np.sin(2 * np.pi * f * t + ph)

# Sinyal cosinus menggunakan library numpy
x_cosinus = A * np.cos(2 * np.pi * f * t + ph)

# Step 4: Plotting kedua sinyal untuk membandingkan
plt.plot(t, x_sinus, label='Sinyal Sinus', color='blue')
plt.plot(t, x_cosinus, label='Sinyal Cosinus', color='orange')

# Menambahkan keterangan pada grafik
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Perbandingan Sinyal Sinus dan Cosinus')
plt.legend()
plt.show()