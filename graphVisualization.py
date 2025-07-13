import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Parameters
G = 1.0            # Gravitational constant 
M = 10.0           # Mass value
x0, y0 = 0.0, 0.0  # Position of the mass
epsilon = 0.1      # Small value to avoid division by zero

# 2D grid
grid_size = 100
space_range = 5
x = np.linspace(-space_range, space_range, grid_size)
y = np.linspace(-space_range, space_range, grid_size)
X, Y = np.meshgrid(x, y)

# Gravitational potential function
def spacetime_warp(X, Y, x0, y0, M, G, epsilon):
    R_squared = (X - x0)**2 + (Y - y0)**2 + epsilon
    Z = -G * M / np.sqrt(R_squared)
    return Z

Z = spacetime_warp(X, Y, x0, y0, M, G, epsilon)

# Plotting spacetime curvature
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 3D surface plot
surface = ax.plot_surface(X, Y, Z, cmap='plasma', linewidth=0, antialiased=True)

# Labels and title
ax.set_title("Spacetime Fabric Warped by Mass", fontsize=15)
ax.set_xlabel('X space')
ax.set_ylabel('Y space')
ax.set_zlabel('Spacetime Curvature')

# color bar to indicate curvature intensity
fig.colorbar(surface, shrink=0.5, aspect=10, label='Warp Depth (Time Dilation)')


plt.show()
