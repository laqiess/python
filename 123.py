import time
import numpy as np

# Генерация матриц
n = 1000
m = 1000
p = 1000

matrix1_list = [[1.0 for _ in range(m)] for _ in range(n)]
matrix2_list = [[1.0 for _ in range(p)] for _ in range(m)]

matrix1_np = np.ones((n, m))
matrix2_np = np.ones((m, p))

# Перемножение матриц с использованием списков Python
start_time = time.time()
result_list = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*matrix2_list)] for row_a in matrix1_list]
time_list = time.time() - start_time

# Перемножение матриц с использованием numpy array
start_time = time.time()
result_np = np.dot(matrix1_np, matrix2_np)
time_np = time.time() - start_time

print("Время перемножения матриц (списки Python):", time_list)
print("Время перемножения матриц (NumPy array):", time_np)
