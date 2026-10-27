# Шпаргалка · CSV, JSON и YAML

<sub>[← Условие](README.md) · [Теория](THEORY.md)</sub>

## CSV

| Задача | Код |
|---|---|
| строки из текста | `lines = [l for l in text.splitlines() if l.strip()]` |
| заголовок | `header = [c.strip() for c in lines[0].split(",")]` |
| запись словарём | `dict(zip(header, [c.strip() for c in line.split(",")]))` |
| пустой вход | `if not lines: return []` |

## JSON

| Задача | Код |
|---|---|
| подключить | `import json` |
| текст → объекты | `json.loads(text)` |
| объекты → текст | `json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)` |
| прочитать файл | `json.load(open(path, encoding="utf-8"))` |

## YAML (учебное подмножество)

| Задача | Код |
|---|---|
| убрать комментарий | `line = raw.split("#", 1)[0].rstrip()` |
| разбить пару | `key, sep, value = line.partition(":")` |
| начало списка | `if not value.strip(): settings[key] = []` |
| элемент списка | `if line.lstrip().startswith("- "): ...` |
| число или строка | `try: int(v) / float(v) except ValueError: v` |
| логическое значение | `v.lower() in ("true", "yes")` |

## Объединение

| Задача | Код |
|---|---|
| взять дополнение | `addition = extra.get(str(row.get(key, "")), {})` |
| запись важнее справочника | `combined = dict(addition); combined.update(row)` |
| проверить обязательные поля | `missing = {"id", "цена"} - set(record)` |

## Частые ошибки

| Симптом | Причина | Что сделать |
|---|---|---|
| в JSON `Азов` | не задан `ensure_ascii=False` | добавить параметр |
| порядок ключей скачет | нет `sort_keys=True` | добавить параметр |
| `3,5` стало строкой | запятая вместо точки | `value.replace(",", ".")` перед `float` |
| комментарий попал в значение | не отрезали часть после `#` | `split("#", 1)[0]` |
| список пустой | строка `ключ:` не открыла список | проверять пустое значение после `:` |
| справочник затёр данные записи | порядок `update` обратный | сначала справочник, потом запись |
| запись пропала | её не было в справочнике и её отбросили | оставлять записи без пары |
