import numpy as np
import matplotlib.pyplot as plt

# define the x values
x = np.linspace(0, 10, 100)

# define the y values for each function
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x)

# plot the functions with different colors and linestyles
plt.plot(x, y1, 'r-', label='sin(x)')
plt.plot(x, y2, 'g--', label='cos(x)')
plt.plot(x, y3, 'b:', label='exp(-x)')

# add a legend and title
plt.legend()
plt.title('Plot of sin(x), cos(x), and exp(-x)')

# show the plot
plt.show()
