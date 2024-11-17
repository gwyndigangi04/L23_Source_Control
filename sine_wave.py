# code was borrowed from: https://www.geeksforgeeks.org/plotting-sine-and-cosine-graph-using-matloplib-in-python/

import numpy as np
import matplotlib.pyplot as plt

# Creating x-axis with range and y-axis with Sine
# Function for Plotting Sine Graph
x = np.arange(0, 2*np.pi, 0.01)
frequency = 15
amp = 3
y = amp*np.sin(x * frequency)

# Plotting Sine Graph
plt.plot(x, y, color='purple')
plt.show()