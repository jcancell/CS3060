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
plt.figure(figsize=(12, 6))

# Plot each row from Matrix A
for i in range(data_A.shape[0]):
    y = data_A[i, :].copy()
    y[y == 10] = np.nan  # Replace 10s with NaN to prevent plotting
    plt.plot(y, label=f'A Gen {i}', linestyle='-', marker='o')

# Plot each row from Matrix B
for i in range(data_B.shape[0]):
    y = data_B[i, :].copy()
    y[y == 10] = np.nan
    plt.plot(y, label=f'B Gen {i}', linestyle='--',marker='x')

plt.title('Fitness Curves: Variant A and B')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.legend(loc='best', fontsize='small')
plt.grid(True)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()