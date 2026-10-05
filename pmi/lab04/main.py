"""Отчёт по журналу наблюдений: чтение входа, вызов функций, печать.

Печатает три строки: разобрано записей, пропущено строк,
средняя температура самого тёплого города (один знак после точки).
"""
import sys

from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
