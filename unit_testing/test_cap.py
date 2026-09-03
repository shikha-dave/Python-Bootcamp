from importlib.metadata.diagnose import inspect
import unittest
import cap
import inspect

class TestCap(unittest.TestCase):
    for item in dir(unittest):
        if not item.startswith("_"):
            obj = getattr(unittest, item)

            if inspect.isclass(obj):
                print(item)

    def test_one_word(self):
        text = "python"
        result = cap.cap_text(text)
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        text = "hello world"
        result = cap.cap_text(text)
        self.assertEqual(result, "Hello World")

    def test_empty_string(self):
        text = ""
        result = cap.cap_text(text)
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()
