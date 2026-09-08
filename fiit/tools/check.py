#!/usr/bin/env python3
"""Local checks for one's own code. Not a sandbox or authoritative grading service."""
import argparse
import io
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description="Самопроверка опубликованной практики")
    parser.add_argument("lab", help="Например, lab01")
    args = parser.parse_args()
    data = json.loads((ROOT / "course.json").read_text(encoding="utf-8"))
    entry = next((x for x in data["assignments"] if x["path"] == args.lab), None)
    if entry is None:
        print("Неизвестная практика. См. course.json.")
        return 2
    if entry["status"] != "published":
        print("Практика ещё не выдана. Тесты не запускались.")
        return 2
    folder = ROOT / entry["path"]
    missing = [name for name in entry["required_files"] if not (folder / name).is_file()]
    if missing:
        print("Ошибка структуры: отсутствуют " + ", ".join(missing))
        return 2
    if entry["grading"]["mode"] == "manual":
        print("Структура: OK. Практику проверяет преподаватель; автотесты не применяются.")
        return 2
    test_dir = ROOT / entry["grading"]["test_directory"]
    suite = unittest.defaultTestLoader.discover(str(test_dir), pattern="test_*.py")
    count = suite.countTestCases()
    expected = entry["grading"]["public_test_count"]
    if count == 0 or count != expected:
        print(f"Ошибка комплекта тестов: найдено {count}, ожидалось {expected}. Оценка не рассчитана.")
        return 2
    result = unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)
    passed = result.testsRun - len(result.failures) - len(result.errors) - len(result.skipped) - len(result.expectedFailures) - len(result.unexpectedSuccesses)
    summary = {"lab": args.lab, "total": result.testsRun, "passed": passed,
               "failed": len(result.failures), "errors": len(result.errors), "skipped": len(result.skipped),
               "scope": "local_public_tests"}
    print(f"\nПройдено {passed} из {result.testsRun}. Это локальная самопроверка.")
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if passed == result.testsRun else 1

if __name__ == "__main__":
    raise SystemExit(main())
