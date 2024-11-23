import unittest
from noun_extraction.extractor import extract_nouns

class TestNounExtraction(unittest.TestCase):
    def test_extract_nouns(self):
        text = "Київ — це столиця України. Дніпро — велика річка."
        expected = ["Київ", "столиця", "України", "Дніпро", "річка"]  
        self.assertEqual(extract_nouns(text), expected)

if __name__ == "__main__":
    unittest.main()
