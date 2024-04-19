#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from multiprocessing import Process, Pool, Array

def calculate_element(i, j, matrix1, matrix2, result, rows):
    # Подсчёт элементов в матрице-результате
    res = 0
    for k in range(rows):
        res += matrix1[i][k] * matrix2[k][j]
    result[i * len(matrix2[0]) + j] = res

def multiply_matrices(matrix1, matrix2, result, num_processes):
    # Умножение матриц с мультипроцессорными вычислениями
    rows = len(matrix1)
    cols = len(matrix2[0])

    processes = []
    for i in range(rows):
        for j in range(cols):
            process = Process(target=calculate_element, args=(i, j, matrix1, matrix2, result, len(matrix2)))
            processes.append(process)
            process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[2, 0], [1, 2]]

    # Создание результирующей матрицы
    result = Array('i', [0] * len(matrix1) * len(matrix2[0]))

    # Процесс умножения
    num_processes = 4  # Тут можно менять по своему желанию
    multiply_matrices(matrix1, matrix2, result, num_processes)

    # Преобразование результата в матрицу
    result_matrix = [[result[i * len(matrix2[0]) + j] for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

    print(result_matrix)
