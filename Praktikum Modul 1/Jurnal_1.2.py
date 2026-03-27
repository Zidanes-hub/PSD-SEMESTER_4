import numpy as np
import matplotlib.pyplot as plt
import scipy.signal # Library tambahan (di luar modul) untuk mendeteksi puncak

# Step 1: Generate Variable independence (variabel t)
# Menggenerate bilangan antara 0 dan 1, sebanyak 1000 bilangan
t = np.linspace(0, 1, 1000) 

# Step 2: Mendefinisikan variable lain (sesuai contoh modul)
A = 3  # Amplitude of sine wave
f = 3  # Frequency of sine wave
ph = 0 # Phase of sine wave

# Step 3: Generate sinyal sinus sesuai dengan persamaan
x = A * np.sin(2 * np.pi * f * t + ph)

# Step 4: Mencari indeks di mana puncak terjadi (Bukit gelombang)
# Fungsi ini akan mengecek nilai yang lebih tinggi dari nilai sekitarnya
peaks, _ = scipy.signal.find_peaks(x)

# Step 5: Plotting the sine wave beserta puncaknya
plt.plot(t, x, label="Sinyal Sinus")

# Menandai puncak yang telah ditemukan pada koordinat (t[peaks], x[peaks])
# Diberi tanda 'x' berwarna merah
plt.plot(t[peaks], x[peaks], "x", color="red", markersize=10, label="Puncak Sinyal")

# Menambahkan label dan judul grafik
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('A={}V, F={} Hz, $\phi={}^\circ$ dengan Puncak'.format(A, f, ph))
plt.legend()

# Menampilkan grafik
plt.show()