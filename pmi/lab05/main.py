"""Отчёт по журналу событий: чтение файла, подсчёты, запись отчёта.

Печатает три числа: всего строк, из них ERROR, из них испорченных.
Затем записывает отчёт в report.txt.
"""
import sys

from logstats import count_levels, format_report, top_errors

path = sys.stdin.readline().strip() or "events.log"
