import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import binom, norm
import os
import csv
import argparse

# Ensure the results directory exists
if not os.path.exists('results'):
    os.makedirs('results')

# Using argparse to handle command-line arguments more reliably
parser = argparse.ArgumentParser(description='Galton Board Simulation')
parser.add_argument('--iteration', type=int, default=1, help='Iteration number for the run')

args = parser.parse_args()
iteration = args.iteration  # Get the iteration number from the arguments

def galtonboard_simulation_matrix(n, N):
    counts = np.zeros(n + 1)
    for _ in range(N):
        position = 0
        for _ in range(n):
            position += np.random.choice([0, 1])  # Move left or right with probability 1/2
        counts[position] += 1
    
    empirical_probs = counts / N
    return counts, empirical_probs

def plot_error_vs_n(N, max_n, iteration):
    bin_errors_mse_n = []
    nor_errors_mse_n = []
    n_values = np.arange(5, max_n + 1, 5)
    
    for n in n_values:
        counts, empirical_probs = galtonboard_simulation_matrix(n, N)
        k = np.arange(0, n + 1)
        binomial_probs = binom.pmf(k, n, 0.5)
        mu = n / 2
        sigma = np.sqrt(n / 4)
        normal_approx = norm.pdf(k, mu, sigma)
        
        mse_bin_emp_n = np.mean((binomial_probs - empirical_probs) ** 2)
        mse_nor_emp_n = np.mean((normal_approx - empirical_probs) ** 2)
        bin_errors_mse_n.append(mse_bin_emp_n)
        nor_errors_mse_n.append(mse_nor_emp_n)
    # Save the data to a CSV file with the iteration number
    with open(f'results_n_1/error_vs_n_{iteration}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["n", "MSE_Binomial_Empirical", "MSE_Normal_Empirical"])
        writer.writerows(zip(n_values, bin_errors_mse_n, nor_errors_mse_n))


def plot_error_vs_N(n, max_N, iteration):
    errors_binomial_N = []
    errors_normal_N = []
    N_values = np.arange(1000, max_N + 1, 200)
    
    for N in N_values:
        counts, empirical_probs = galtonboard_simulation_matrix(n, N)
        k = np.arange(0, n + 1)
        binomial_probs = binom.pmf(k, n, 0.5)
        mu = n / 2
        sigma = np.sqrt(n / 4)
        normal_approx = norm.pdf(k, mu, sigma)
        
        mse_bin_emp_N = np.mean((binomial_probs - empirical_probs) ** 2)
        mse_nor_emp_N = np.mean((normal_approx - empirical_probs) ** 2)
        
        errors_binomial_N.append(mse_bin_emp_N)
        errors_normal_N.append(mse_nor_emp_N)
    # Save the data to a CSV file with the iteration number
    with open(f'results_N/error_vs_N_{iteration}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["N", "MSE_Binomial_Empirical", "MSE_Normal_Empirical"])
        writer.writerows(zip(N_values, errors_binomial_N, errors_normal_N))

def plot_galton_board_simulation(n, N, iteration):
    counts, empirical_probs = galtonboard_simulation_matrix(n, N)
    k = np.arange(0, n + 1)
    binomial_probs = binom.pmf(k, n, 0.5)
    mu = n / 2
    sigma = np.sqrt(n / 4)
    normal_approx = norm.pdf(k, mu, sigma)


# Example usage: the iteration number is passed as an argument
plot_error_vs_n(N=5000, max_n=50, iteration=iteration)
#plot_error_vs_N(n=10, max_N=5000, iteration=iteration)
plot_galton_board_simulation(n=10, N=5000, iteration=iteration)