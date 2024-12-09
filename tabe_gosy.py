import numpy as np
import matplotlib.pyplot as plt
import math

means = [15, 30, 45]
std_devs = [1, 2, 5]

x = np.linspace(-50, 150, 1000)  
plt.figure(figsize=(15, 10))

for i, mean in enumerate(means):
    for j, std_dev in enumerate(std_devs):
        plt.subplot(3, 3, i * 3 + j + 1)  
        y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
        plt.plot(x, y)
        plt.title(f'Mean={mean}, Std Dev={std_dev}')
        plt.xlabel('X')
        plt.ylabel('Probability Density')
        plt.grid(True)
plt.tight_layout() 
plt.show()