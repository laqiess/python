import time
import numpy as np

# Создаем две матрицы размерностью 1000x1000 как списки Python
matrix1_list = [[1] * 100 for _ in range(1000)]
matrix2_list = [[1] * 100 for _ in range(1000)]

# Функция для умножения двух матриц представленных как списки Python
def multiply_matrices_list(matrix1, matrix2):
    result = [[1] * 100 for _ in range(1000)]  # Изначально заполняем нулями
    for i in range(100):
        for j in range(100):
            for k in range(100):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# Замеряем время умножения
start_time = time.time()
for _ in range(2):  # Повторяем операцию для надежности
    result_list = multiply_matrices_list(matrix1_list, matrix2_list)
end_time = time.time()
print("Time taken to multiply matrices using Python lists: ", end_time - start_time)


# Создаем матрицы размерностью 100x100 как numpy arrays
matrix1_np = np.ones((100, 100))
matrix2_np = np.ones((100, 100))

# Замеряем время умножения
start_time = time.time()
for _ in range(2):  # Повторяем операцию для надежности
    result_np = np.dot(matrix1_np, matrix2_np)
end_time = time.time()
print("Time taken to multiply matrices using NumPy arrays: ", end_time - start_time)