import numpy as np
import matplotlib.pyplot as plt

# Step 1: Defining the time axis (rentang waktu dari -1 hingga 1)
t = np.linspace(-1, 1, 1000)

# Step 2: Defining the parameter 'alpha'
a = 5  
b = -5 

# Step 3: Generation of function (x = e^(alpha * t))
x1 = np.exp(a * t)
x2 = np.exp(b * t)

# Step 4: Plotting of the function
plt.figure(figsize=(8, 6))

# Plot untuk sinyal eksponensial naik
plt.subplot(2, 1, 1)
plt.plot(t, x1)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title(f'Exponentially growing function (a={a})')

# Plot untuk sinyal eksponensial turun
plt.subplot(2, 1, 2)
plt.plot(t, x2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title(f'Exponentially decaying function (b={b})')

plt.tight_layout()
plt.show()