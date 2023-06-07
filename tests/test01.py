import unittest
import sys
sys.path.insert(1, "../cli")
import funcs

class TestWC(unittest.TestCase):
    '''
    Contains the 3 basic unit tests to check the functionality of wc tool
    '''
    def setUp(self) -> None:
        self.byte_count = funcs.get_bytes("sample_text.txt")
        self.word_count = funcs.get_words("sample_text.txt")
        self.line_count = funcs.get_lines("sample_text.txt")
        self.all_count  = funcs.get_all("sample_text.txt")

    def test_c(self):
        '''Ensures that the byte count is correct'''
        self.assertEqual(self.byte_count, 334695, "Incorrect byte count value")

    def test_w(self):
        '''Ensures that the word count is correct'''
        self.assertEqual(self.word_count, 58159, "Incorrect word count value")

    def test_l(self):
        '''Ensures that the line count is correct'''
        self.assertEqual(self.line_count, 7136, "Incorrect line count value")