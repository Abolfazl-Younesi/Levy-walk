This repository contains a Python implementation of the Lévy Walk simulation, a random walk model with a power-law step length distribution. The code simulates multiple walkers with boundary conditions and visualizes their trajectories for different values of the power-law exponent.

# Lévy Walk Simulation

This repository provides a Python implementation of the Lévy Walk simulation, a random walk model where the step lengths are drawn from a power-law distribution. The code simulates multiple walkers with boundary conditions and visualizes their trajectories for different values of the power-law exponent.

## Features

- Simulate Lévy Walk for multiple walkers with boundary conditions
- Generate step lengths from a power-law distribution
- Plot the trajectories of walkers for different power-law exponents

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/levy-walk-simulation.git
   ```

2. Navigate to the project directory:

   ```bash
   cd levy-walk-simulation
   ```

3. Run the simulation script:

   ```bash
   python levy_walk.py
   ```

   This will generate a figure titled `LW.png` containing 12 subplots, each showing the trajectories of 3 walkers for a different power-law exponent ranging from 0.5 to 2.5.

## Code Overview

The repository contains the following Python file:

- `levy_walk.py`: This file contains two main functions:
  - `levy_walk(n_walkers, n_steps, alpha, x_range, y_range)`: Simulates the Lévy Walk for multiple walkers with boundary conditions.
  - `plot_trajectories(trajectories, alpha, ax)`: Plots the trajectories of multiple walkers on a given Matplotlib axes.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


This repository contains a Python script that simulates the Lévy Walk for multiple walkers with boundary conditions. The script generates and plots the trajectories of the walkers for different values of the power-law exponent. Feel free to customize the content of the README file according to your specific requirements.
