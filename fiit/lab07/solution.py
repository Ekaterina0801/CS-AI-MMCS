# Лабораторная 07. NumPy I: массивы, форма, индексация
#
# Считайте через NumPy, без циклов по элементам.
# Дробные результаты округляйте до шести знаков, возвращайте обычные списки и числа.
#
# reshape_rows(values, width)   -> таблица по width значений в строке; не делится нацело -> []
# block(matrix, rows, columns)  -> участок таблицы: указанные строки и столбцы
# column_means(matrix)          -> среднее по каждому столбцу
# column_range(matrix, column)  -> размах значений в столбце
#
# Условие целиком: README.md рядом с этим файлом.
import numpy as np


def reshape_rows(values, width):
    ...


def block(matrix, rows, columns):
    ...


def column_means(matrix):
    ...


def column_range(matrix, column):
    ...
