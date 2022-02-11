import dataclasses
import unittest

from magicModule import *


class TestMagicList(unittest.TestCase):
    def test_numbers_magic_list(self):
        magic_list = MagicList()
        magic_list[0] = 5
        expected_list = [5]

        self.assertEqual(str(magic_list), str(expected_list))

    def test_magic_list_index_error_on_continuity(self):
        magic_list = MagicList()
        with self.assertRaises(IndexError):
            magic_list[1] = 3

    def test_dataclass_magic_list(self):
        @dataclasses.dataclass
        class Person:
            age: int = 1

        persons_magic_list = MagicList(cls_type=Person)
        persons_magic_list[0].age = 5
        expected = [Person(age=5)]

        self.assertEqual(str(expected), str(persons_magic_list))

    def test_dataclass_index_error_on_continuity(self):
        @dataclasses.dataclass
        class Person:
            age: int = 1

        persons_magic_list = MagicList(cls_type=Person)
        with self.assertRaises(IndexError):
            persons_magic_list[1].age = 5


if __name__ == '__main__':
    unittest.main()
