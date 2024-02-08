import unittest
import pytest
import sys
import project
from app import PythonQuizApp


class TestPythonQuizApp(unittest.TestCase):

    def test_close(self):
        quiz = PythonQuizApp()
        self.assertFalse(quiz.window.winfo_exists()) 
        quiz.close()
        self.assertFalse(quiz.window.winfo_exists())

    def test_github(self):
        quiz = PythonQuizApp()
        self.assertIsNone(quiz.github())

    def test_setup_gui(self):
        quiz = PythonQuizApp()
        quiz.setup_gui()
        self.assertTrue(quiz.window.winfo_exists())


if __name__ == '__main__':
    unittest.main()
