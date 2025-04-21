import numpy as np
import matplotlib.pyplot as plt

data_A = np.load('fitness_matrix_A.npy')

data_B = np.load('fitness_matrix_B.npy')

data_C = np.load('fitness_matrix_C.npy')

data_D = np.load('fitness_matrix_D.npy')

# Convert any sentinel values (e.g., 10) to NaN so they are ignored in averaging
data_A = np.where(data_A == 10000, np.nan, data_A)
data_B = np.where(data_B == 10000, np.nan, data_B)
data_C = np.where(data_C == 10000, np.nan, data_C)
data_D = np.where(data_D == 10000, np.nan, data_D)

# Compute average fitness per generation (i.e., column-wise mean)
avg_fitness_A = np.nanmean(data_A, axis=0)
avg_fitness_B = np.nanmean(data_B, axis=0)
avg_fitness_C = np.nanmean(data_C, axis=0)
avg_fitness_D = np.nanmean(data_D, axis=0)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(avg_fitness_A, label='Variant A', marker='o')
plt.plot(avg_fitness_B, label='Variant B', marker='o', linestyle='--')
plt.plot(avg_fitness_C, label='Variant C', marker='o', linestyle=':')
plt.plot(avg_fitness_D, label='Variant D', marker='o', linestyle='-.')
plt.title('Average Fitness Over Generations')
plt.xlabel('Generation')
plt.ylabel('Average Fitness')
plt.legend()
plt.grid(True)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()