import unittest

from jsonNormalizer import JsonNormalizer


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._json = [{"name": "device",
                       "strVal": "IPhone",
                       "metadata": "not interesting"},
                      {"name": "isBlue",
                       "boolVal": "false",
                       "lastSeen": "something"}]

    def test_something(self):
        self.assertEqual(str(JsonNormalizer.normalize(self._json)),
                         "{'isBlue': 'false', 'device': 'IPhone'}")


if __name__ == '__main__':
    unittest.main()
