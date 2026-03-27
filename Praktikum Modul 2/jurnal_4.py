import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# STEP 1: Menyiapkan sinyal suara
fs = 8000 # Sampling rate
f = 1000  # Frekuensi sinyal suara buatan
t = np.linspace(0, 1, fs) 
x_suara = np.sin(2 * np.pi * f * t)

# STEP 2: Mendefinisikan parameter eksponensial
a = -5  # Decaying factor (parameter eksponensial turun)
b = 5   # Growing factor (parameter eksponensial naik)

# STEP 3: Menerapkan fungsi eksponensial ke sinyal suara
x_volume_turun = x_suara * np.exp(a * t) 
x_volume_naik = x_suara * np.exp(b * t)  

# STEP 4: Mendengarkan hasil output 
print("Memutar suara dengan volume menurun (fade-out)...")
sd.play(x_volume_turun, fs)
sd.wait() 

print("Memutar suara dengan volume menaik (fade-in)...")
sd.play(x_volume_naik, fs)
sd.wait()

# STEP 5: Visualisasi sinyal untuk laporan
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x_volume_turun)
plt.ylabel('Amplitude')
plt.title('Sinyal Suara: Volume Menurun (Fade-Out)')

plt.subplot(2, 1, 2)
plt.plot(t, x_volume_naik, color='orange')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Sinyal Suara: Volume Menaik (Fade-In)')

plt.tight_layout()
plt.show()