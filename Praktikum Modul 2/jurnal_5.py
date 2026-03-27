import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generation of signals
t = np.linspace(0, 1, 1000)
f = 5
x1 = np.sin(2 * np.pi * f * t)      # Sinyal Stasioner
x2 = np.sin(2 * np.pi * f * t**2)   # Sinyal Non-stasioner

# Step 2: Plotting of signals
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(t, x1)
plt.xlabel('Time (t)'), plt.ylabel('Amplitude'), plt.title('Stationary signal')

plt.subplot(2, 1, 2)
plt.plot(t, x2, 'r')
plt.xlabel('Time (t)'), plt.ylabel('Amplitude'), plt.title('Non-stationary signal')
plt.tight_layout()
plt.show()


# EKSPERIMEN 2: Generation of Chirp Signal (Non-stationary)
from scipy.signal import chirp

# Step 1: Generation of chirp signal
t_chirp = np.linspace(0, 10, 10000)
c1 = chirp(t_chirp, f0=10, f1=1, t1=10, method='linear')
c2 = chirp(t_chirp, f0=10, f1=1, t1=10, method='quadratic')
c3 = chirp(t_chirp, f0=10, f1=1, t1=10, method='logarithmic')
c4 = chirp(t_chirp, f0=10, f1=1, t1=10, method='hyperbolic')

# Step 2: Plotting the signals
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1), plt.plot(t_chirp, c1), plt.xlabel('Time (t)'), plt.ylabel('Amplitude (V)'), plt.title('Linear chirp')
plt.subplot(2, 2, 2), plt.plot(t_chirp, c2), plt.xlabel('Time (t)'), plt.ylabel('Amplitude (V)'), plt.title('Quadratic chirp')
plt.subplot(2, 2, 3), plt.plot(t_chirp, c3), plt.xlabel('Time (t)'), plt.ylabel('Amplitude (V)'), plt.title('Logarithmic chirp')
plt.subplot(2, 2, 4), plt.plot(t_chirp, c4), plt.xlabel('Time (t)'), plt.ylabel('Amplitude (V)'), plt.title('Hyperbolic chirp')
plt.tight_layout()
plt.show()