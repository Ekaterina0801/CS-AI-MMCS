# Шпаргалка · Текстовые файлы

<sub>[← Условие](README.md) · [Теория](THEORY.md)</sub>

## Чтение

| Задача | Код |
|---|---|
| открыть на чтение | `with open(path, encoding="utf-8") as log:` |
| перебрать строки | `for line in log:` |
| убрать перевод строки | `line.rstrip("\n")` |
| убрать пробелы по краям | `line.strip()` |
| пропустить пустую строку | `if not line.strip(): continue` |
| прочитать имя файла из ввода | `path = sys.stdin.readline().strip()` |

Не используйте `read()` и `readlines()`: они тянут весь файл в память.

## Запись

| Задача | Код |
|---|---|
| записать с нуля | `with open("report.txt", "w", encoding="utf-8") as out:` |
| записать текст | `out.write(text)` |
| дописать в конец | режим `"a"` |
| собрать текст из строк | `"\n".join(lines) + "\n"` |

## Разбор строки журнала

| Задача | Код |
|---|---|
| три части, сообщение целиком | `parts = line.strip().split(maxsplit=2)` |
| проверить число частей | `if len(parts) < 3: raise ValueError(...)` |
| распаковать | `time, level, message = parts` |
| проверить уровень | `if level not in ("DEBUG", "INFO", "WARNING", "ERROR"):` |

## Подсчёты

| Задача | Код |
|---|---|
| счётчик по ключу | `counts[level] = counts.get(level, 0) + 1` |
| сумма значений словаря | `sum(counts.values())` |
| значение с запасным вариантом | `counts.get("ERROR", 0)` |
| частые записи по убыванию | `sorted(counts.items(), key=lambda p: (-p[1], p[0]))` |
| первые n | `ordered[:n]` |

## Ошибки

| Задача | Код |
|---|---|
| сообщить о негодной строке | `raise ValueError("...")` |
| пропустить негодную строку | `try: ... except ValueError: continue` |

## Частые ошибки

| Симптом | Причина | Что сделать |
|---|---|---|
| `FileNotFoundError` | программа запущена не из той папки | `cd lab05`, затем `python main.py` |
| `UnicodeDecodeError` или кракозябры | не указан `encoding="utf-8"` | указать явно |
| второй проход даёт пустоту | файл уже дочитан до конца | открыть его ещё раз или `log.seek(0)` |
| сообщение обрезано | `split()` без `maxsplit` | `split(maxsplit=2)` |
| в отчёте лишние переводы строк | не убран `\n` у прочитанной строки | `line.rstrip("\n")` |
| журнал исчез | открыли его в режиме `"w"` | восстановить из репозитория: `git restore lab05/events.log` |
| отчёт пустой | забыли `with` или не вызвали `write` | писать внутри блока `with` |
