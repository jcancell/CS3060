import numpy as np
import matplotlib.pyplot as plt

data_A = np.load('fitness_matrix_A.npy')
print('Matrix A')
print(data_A)
print("")

data_B = np.load('fitness_matrix_B.npy')
print('Matrix B')
print(data_B)
print("")

#plt.plot(data_A[0,:])

#plt.show()

# Plot both A and B rows on the same plot
# Convert any sentinel values (e.g., 10) to NaN so they are ignored in averaging
data_A = np.where(data_A == 10000, np.nan, data_A)
data_B = np.where(data_B == 10000, np.nan, data_B)

# Compute average fitness per generation (i.e., column-wise mean)
avg_fitness_A = np.nanmean(data_A, axis=0)
avg_fitness_B = np.nanmean(data_B, axis=0)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(avg_fitness_A, label='Variant A', marker='o')
plt.plot(avg_fitness_B, label='Variant B', marker='o', linestyle='--')
plt.title('Average Fitness Over Generations')
plt.xlabel('Generation')
plt.ylabel('Average Fitness')
plt.legend()
plt.grid(True)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()