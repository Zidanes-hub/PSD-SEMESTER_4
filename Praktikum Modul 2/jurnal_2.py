import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generation of signals x1(t) and x2(t)
t = np.linspace(-1, 1, 100)
f = 5

# Sinyal eksponensial kompleks x1 = e^(j*2*pi*f*t) dan x2 = e^(-j*2*pi*f*t)
x1 = np.exp(1j * 2 * np.pi * f * t)
x2 = np.exp(-1j * 2 * np.pi * f * t)

# Step 2: Plotting the signals, its magnitude, and phase
plt.figure(figsize=(10, 8))

# Plot Sinyal Asli
plt.subplot(3, 2, 1)
plt.plot(t, x1.real)
plt.xlabel('Time (t)'), plt.ylabel('Amplitude (V)'), plt.title('$e^{j\Omega t}$')

plt.subplot(3, 2, 2)
plt.plot(t, x2.real)
plt.xlabel('Time (t)'), plt.ylabel('Amplitude (V)'), plt.title('$e^{-j\Omega t}$')

# Plot Respon Magnitudo 
plt.subplot(3, 2, 3)
plt.plot(t, np.abs(x1))
plt.xlabel('Time (t)'), plt.ylabel('Magnitude (V)'), plt.title('|$e^{j\Omega t}$|')

plt.subplot(3, 2, 4)
plt.plot(t, np.abs(x2))
plt.xlabel('Time (t)'), plt.ylabel('Magnitude (V)'), plt.title('|$e^{-j\Omega t}$|')

# Plot Respon Fase 
plt.subplot(3, 2, 5)
plt.plot(t, np.angle(x1) * 180 / np.pi) 
plt.xlabel('Time (t)'), plt.ylabel('$Phase(^\circ$)'), plt.title('$\Phi(x_1(t))$')

plt.subplot(3, 2, 6)
plt.plot(t, np.angle(x2) * 180 / np.pi)
plt.xlabel('Time (t)'), plt.ylabel('$Phase(^\circ$)'), plt.title('$\Phi(x_2(t))$')

plt.tight_layout()
plt.show()