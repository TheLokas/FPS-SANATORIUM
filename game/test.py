import unittest
from function_ren import *

class TestJSON(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(CheckJSON("test/empty_test.json"), False)

    def test_empty_file(self):
        self.assertEqual(CheckJSON("test/empty_file_test.json"), False)

    def test_not_json_file(self):
        self.assertEqual(CheckJSON("test/not_json_test.json"), False)

    def test_no_scenes(self):
        self.assertEqual(CheckJSON("test/no_scenes_test.json"), False)

    def test_true1(self):
        self.assertEqual(CheckJSON("test/true_test1.json"), True)

    def test_false1(self):
        self.assertEqual(CheckJSON("test/false_test1.json"), False)

    def test_true2(self):
        self.assertEqual(CheckJSON("test/true_test2.json"), True)

    def test_false2(self):
        self.assertEqual(CheckJSON("test/false_test2.json"), False)

    def test_true3(self):
        self.assertEqual(CheckJSON("test/true_test3.json"), True)

    def test_false3(self):
        self.assertEqual(CheckJSON("test/false_test3.json"), False)

class TestGame(unittest.TestCase):
    
    def test_JSON(self):
        self.assertEqual(CheckJSON("1.json"), True)

    def test_Files(self):
        self.assertEqual(GetNotInDirectoryFilenames(), ['1.json', '2.json', 'function.rpyc', 'function_ren.py', 'gui.rpy', 'gui.rpyc', 'options.rpy', 'options.rpyc', 'saves.json', 'screens.rpy', 'screens.rpyc', 'script.rpy', 'script.rpyc', 'test.py'])

    def test_GetJSON(self):
        self.assertEqual(GetFilenames(), ['1.json', '2.json'])

if __name__ == "__main__":
    unittest.main()
