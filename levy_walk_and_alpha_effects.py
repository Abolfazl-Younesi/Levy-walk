"""# Levy walk with bound"""

import numpy as np
import matplotlib.pyplot as plt

def levy_walk(n_walkers, n_steps, alpha, x_range, y_range):
    """
    Simulate Lévy Walk for multiple walkers with boundary conditions.

    Args:
        n_walkers (int): Number of walkers.
        n_steps (int): Number of steps for each walker.
        alpha (float): Power-law exponent for the step length distribution.
        x_range (tuple): Range for x coordinates (min, max).
        y_range (tuple): Range for y coordinates (min, max).

    Returns:
        ndarray: Array of walker trajectories with shape (n_walkers, n_steps, 2).
    """
    positions = np.zeros((n_walkers, n_steps, 2))

    for i in range(n_walkers):
        x, y = np.random.uniform(x_range[0], x_range[1]), np.random.uniform(y_range[0], y_range[1])
        for j in range(n_steps):
            # Generate step length from power-law distribution
            step_length = np.random.pareto(alpha)

            # Generate random direction
            theta = np.random.uniform(0, 2 * np.pi)

            # Update position
            new_x = x + step_length * np.cos(theta)
            new_y = y + step_length * np.sin(theta)

            # Check boundary conditions
            if x_range[0] <= new_x <= x_range[1] and y_range[0] <= new_y <= y_range[1]:
                x, y = new_x, new_y

            positions[i, j] = [x, y]

    return positions

def plot_trajectories(trajectories, alpha, ax):
    """
    Plot the trajectories of multiple walkers.

    Args:
        trajectories (ndarray): Array of walker trajectories with shape (n_walkers, n_steps, 2).
        alpha (float): Power-law exponent for the step length distribution.
        ax (matplotlib.axes.Axes): Axes object to plot on.
    """
    n_walkers, _, _ = trajectories.shape
    colors = plt.cm.viridis(np.linspace(0, 1, n_walkers))

    for i in range(n_walkers):
        x, y = trajectories[i, :, 0], trajectories[i, :, 1]
        ax.plot(x, y, color=colors[i], alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Lévy Walk Trajectories (α = {alpha:.1f})')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

# Example usage
n_walkers = 3
n_steps = 500
alphas = np.linspace(0.5, 2.5, 12)
x_range = (0, 100)
y_range = (0, 100)

fig, axes = plt.subplots(3, 4, figsize=(16, 12))

for i, alpha in enumerate(alphas):
    row, col = i // 4, i % 4
    trajectories = levy_walk(n_walkers, n_steps, alpha, x_range, y_range)
    plot_trajectories(trajectories, alpha, axes[row, col])

plt.tight_layout()
plt.savefig("LW.png")
plt.show()
