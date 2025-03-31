import numpy as np
from matplotlib import pyplot as plt

def plot_data(data):
    x = np.arange(len(data))
    y = data
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Plot of the dataset')
    plt.show()

# Example usage:
data_points = [1, 2, 3, 4, 5]
plot_data(data_points)

