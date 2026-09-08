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
        self.check_case('3\n4\n', '12.0\n14.0')

    def test_case_02(self):
        self.check_case('5\n6\n', '30.0\n22.0')

    def test_case_03(self):
        self.check_case('2.5\n4\n', '10.0\n13.0')

    def test_case_04(self):
        self.check_case('3\n3\n', '9.0\n12.0')

    def test_case_05(self):
        self.check_case('1\n1\n', '1.0\n4.0')
