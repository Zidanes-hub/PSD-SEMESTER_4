import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generation of rotating phasor (Sesuai dengan modul)
t = np.linspace(0, 1, 100)
f = 5
x1 = np.exp(1j * 2 * np.pi * f * t)
x2 = np.exp(-1j * 2 * np.pi * f * t)

# Step 2: Generation of sine and cosine wave dari eksponensial kompleks
x_cos = np.real((x1 + x2) / 2)
x_sin = np.real((x1 - x2) / (2 * 1j))

# Step 3: Menjumlahkan nilai kuadrat dari sinyal sinus dan cosinus 
x_kuadrat_jumlah = (x_sin ** 2) + (x_cos ** 2)

# Step 4: Plotting the result
plt.figure(figsize=(8, 6))

# Plot sinyal Cosinus
plt.subplot(3, 1, 1)
plt.plot(t, x_cos)
plt.ylabel('Amplitude (V)')
plt.title('Cosine wave')

# Plot sinyal Sinus
plt.subplot(3, 1, 2)
plt.plot(t, x_sin, color='red')
plt.ylabel('Amplitude (V)')
plt.title('Sine wave')

# Plot hasil penjumlahan kuadrat sinyal sinus dan cosinus
plt.subplot(3, 1, 3)
plt.plot(t, x_kuadrat_jumlah, color='green')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude (V)')
plt.ylim(0, 2) 
plt.title('Hasil $\sin^2(\\theta) + \cos^2(\\theta)$')

plt.tight_layout()
plt.show()