import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ProgramTests(unittest.TestCase):
    def check_case(self, data, expected):
        run = subprocess.run([sys.executable, str(ROOT / "main.py")], input=data, text=True, capture_output=True, timeout=3)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(run.stdout.splitlines(), expected.splitlines())

    def test_case_01(self):
        self.check_case('10\n14\n', '12.0')

    def test_case_02(self):
        self.check_case('14\n10\n', '12.0')

    def test_case_03(self):
        self.check_case('7\n7\n', '7.0')

    def test_case_04(self):
        self.check_case('-6\n6\n', '0.0')

    def test_case_05(self):
        self.check_case('1.5\n2.5\n', '2.0')

    def test_case_06(self):
        self.check_case('-8\n-4\n', '-6.0')
