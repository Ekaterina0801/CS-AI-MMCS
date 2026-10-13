"""Сводка по таблице событий: чтение CSV, подсчёты, запись сводки.

Печатает три числа: записей, различных типов, минут у типа «ошибка».
Затем записывает сводку в summary.csv.
"""
import sys

from tablestats import count_types, read_rows, to_csv, total_minutes

path = sys.stdin.readline().strip() or "events.csv"
