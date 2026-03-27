import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate Variable independence (variabel t)
# Menggenerate 1000 bilangan antara 0 dan 1
t = np.linspace(0, 1, 1000) 

# Step 2: Mendefinisikan variable lain (Sesuai modul)
A = 3  # Amplitude of sine wave
f = 3  # Frequency of sine wave
ph = 0 # Phase of sine wave

# Step 3: Generate sinyal sinus sesuai dengan persamaan
x = A * np.sin(2 * np.pi * f * t + ph)

# Step 4: Menghitung zero crossing (Logika tambahan di luar modul)
# Fungsi np.sign(x) mengubah nilai positif menjadi 1, negatif menjadi -1, dan nol menjadi 0.
# Fungsi np.diff() menghitung selisih antar nilai yang berdekatan. 
# Jika ada perubahan tanda (melewati titik nol), hasil selisihnya tidak akan nol.
zero_crossings = np.where(np.diff(np.sign(x)))

# Menghitung total titik zero crossing yang ditemukan
jumlah_zero_crossing = len(zero_crossings)

# Menampilkan hasil perhitungan pada teks (console)
print("Jumlah zero crossing yang dilalui sinyal adalah:", jumlah_zero_crossing)

# Step 5: Plotting the sine wave beserta titik zero crossing-nya
plt.plot(t, x, label="Sinyal Sinus")

# Menandai titik zero crossing dengan lingkaran ('o') berwarna hijau
plt.plot(t[zero_crossings], x[zero_crossings], "o", color="green", markersize=8, label="Zero Crossing")

# Membuat garis putus-putus hitam pada sumbu X (nilai Y = 0) agar lebih jelas
plt.axhline(0, color='black', linestyle='--', linewidth=1) 

# Menambahkan label dan judul
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title(f'Sinyal Sinus dengan {jumlah_zero_crossing} Titik Zero Crossing')
plt.legend()

# Menampilkan grafik
plt.show()