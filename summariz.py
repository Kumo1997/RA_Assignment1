import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Directories where results are stored
n_directory = 'results_n_1'
N_directory = 'results_N'

def average_results_n(iterations):
    """ Averages the results for 'n' from multiple iterations """
    dfs = []
    for i in range(1, iterations + 1):
        file_path = os.path.join(n_directory, f'error_vs_n_{i}.csv')
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            dfs.append(df)

    if not dfs:
        print(f"No files found in {n_directory}.")
        return

    # Concatenate and group by 'n' to calculate the mean
    df_all = pd.concat(dfs)
    avg_df = df_all.groupby('n').mean().reset_index()

    # Save the averaged data to a new CSV file
    avg_df.to_csv(os.path.join(n_directory, 'average_error_vs_n.csv'), index=False)

    # Plot the averaged data
    plt.figure()
    plt.plot(avg_df['n'], avg_df['MSE_Binomial_Empirical'], 'b--o', label='Avg MSE (Binomial vs Empirical)')
    plt.plot(avg_df['n'], avg_df['MSE_Normal_Empirical'], 'r--o', label='Avg MSE (Normal vs Empirical)')
    plt.title('Average Error vs n')
    plt.xlabel('n (Number of levels)')
    plt.ylabel('Mean Squared Error (MSE)')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(n_directory, 'average_error_vs_n_plot.png'))
    plt.close()


def average_results_N(iterations):
    """ Averages the results for 'N' from multiple iterations """
    dfs = []
    for i in range(1, iterations + 1):
        file_path = os.path.join(N_directory, f'error_vs_N_{i}.csv')
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            dfs.append(df)

    if not dfs:
        print(f"No files found in {N_directory}.")
        return

    # Concatenate and group by 'N' to calculate the mean
    df_all = pd.concat(dfs)
    avg_df = df_all.groupby('N').mean().reset_index()

    # Save the averaged data to a new CSV file
    avg_df.to_csv(os.path.join(N_directory, 'average_error_vs_N.csv'), index=False)

    # Plot the averaged data
    plt.figure()
    plt.plot(avg_df['N'], avg_df['MSE_Binomial_Empirical'], 'b--o', label='Avg MSE (Binomial vs Empirical)')
    plt.plot(avg_df['N'], avg_df['MSE_Normal_Empirical'], 'r--o', label='Avg MSE (Normal vs Empirical)')
    plt.title('Average Error vs N')
    plt.xlabel('N (Number of balls)')
    plt.ylabel('Mean Squared Error (MSE)')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(N_directory, 'average_error_vs_N_plot.png'))
    plt.close()


def average_galton_board_simulation(iterations):
    """ Placeholder function for averaging galton board simulations (if needed) """
    # If you're also averaging the galton board simulations, you can implement this similarly
    pass


if __name__ == '__main__':
    iterations = 10  # Number of iterations (adjust based on your experiment)
    
    # Average and plot results for 'n'
    average_results_n(iterations)
    
    # Average and plot results for 'N'
    average_results_N(iterations)
    
    # Placeholder for galton board simulation averaging
    # average_galton_board_simulation(iterations)