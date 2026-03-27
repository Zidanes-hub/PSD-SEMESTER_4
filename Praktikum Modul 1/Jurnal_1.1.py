import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate Variable independence (variabel t)
t = np.linspace(0, 1, 1000)

# Step 2: Mendefinisikan variable lain (Ubah nilai A dan f di sini)
A = 5 # Ubah amplitudo (misalnya dari 3 menjadi 5)
f = 10 # Ubah frekuensi (misalnya dari 3 menjadi 10)
ph = 0 # Phase of sine wave

# Step 3: Generate sinyal sinus sesuai dengan persamaan
x = A * np.sin(2 * np.pi * f * t + ph)

# Step 4: Plotting the sine wave
plt.plot(t, x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('A={}V, F={} Hz, $\phi={}^\circ$'.format(A, f, ph))
plt.show()