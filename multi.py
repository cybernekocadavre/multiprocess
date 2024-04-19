#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from multiprocessing import Process, Pool

def calculate_element(i, j, matrix1, matrix2, result, rows):
    # Подсчёт элементов в матрице-результате
    
    res = 0
    for k in range(rows):
        res += matrix1[i][k] * matrix2[k][j]
    result[i][j] = res

def multiply_matrices(matrix1, matrix2, result, num_processes):
    #Умножение матриц с мультипроцессорными вычислениями
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


def write_matrix_to_file(matrix, filename):
    
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[2, 0], [1, 2]]

    #Создание результирующей матрицы
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    #Процесс умножения
    num_processes = 4  #Тут можно менять по своему желанию
    multiply_matrices(matrix1, matrix2, result, num_processes)
    
    write_matrix_to_file(result, "result_matrix.txt")


# In[ ]:




