import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate variabel waktu (t)
t = np.linspace(0, 1, 100)

# Step 2: Mendefinisikan parameter frekuensi dan fase
f = 5  # Frekuensi
phi_1, phi_2, phi_3 = 0, 120, 240  # Tiga fase berbeda dalam derajat

# Step 3: Mengubah nilai amplitudo A1, A2, dan A3 (Sesuai instruksi Jurnal III)
A1 = 1  # Amplitudo untuk Phase-1
A2 = 2  # Amplitudo untuk Phase-2
A3 = 3  # Amplitudo untuk Phase-3

# Step 4: Generate 3 sinyal dengan amplitudo yang berbeda-beda
x1 = A1 * np.sin(2 * np.pi * f * t + phi_1 * np.pi / 180)
x2 = A2 * np.sin(2 * np.pi * f * t + phi_2 * np.pi / 180)
x3 = A3 * np.sin(2 * np.pi * f * t + phi_3 * np.pi / 180)

# Step 5: Plotting ketiga sinyal dalam satu grafik
plt.plot(t, x1, 'b', label=f'Phase-1 (A1={A1}V)')
plt.plot(t, x2, 'r', label=f'Phase-2 (A2={A2}V)')
plt.plot(t, x3, 'g', label=f'Phase-3 (A3={A3}V)')

# Menambahkan keterangan pada grafik
plt.xlabel('Time (t)')
plt.ylabel('Amplitude (V)')
plt.title('Sinyal Sinusoidal 3 Fasa dengan Amplitudo Berbeda')
plt.legend(loc=1)
plt.show()