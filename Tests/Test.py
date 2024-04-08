import unittest

import main
from main import auth, register, make_exercise, make_diary


class TestFunctions(unittest.TestCase):

    def test_auth(self):
        self.assertEqual(auth(1), True)

        self.assertEqual(auth(7), False)

    def test_register(self):
        self.assertEqual(register(main.U1), True)

        self.assertEqual(register(main.U3), False)

    def test_make_exercise(self):
        self.assertEqual(make_exercise(main.ex1), True)

        self.assertEqual(make_exercise(main.ex5), False)

    def test_make_diary(self):
        self.assertEqual(make_diary(main.d1), True)

        self.assertEqual(make_diary(main.d3), False)


if __name__ == '__main__':
    unittest.main()
