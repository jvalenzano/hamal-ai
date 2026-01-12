
import unittest
import sys
import os
import json

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.utils import clean_json_output

class TestJsonCleaning(unittest.TestCase):
    
    def test_clean_json(self):
        # Case 1: Pure JSON
        raw = '{"key": "value"}'
        cleaned = clean_json_output(raw)
        self.assertEqual(json.loads(cleaned), {"key": "value"})
        
    def test_markdown_json(self):
        # Case 2: Markdown fences
        raw = '```json\n{"key": "value"}\n```'
        cleaned = clean_json_output(raw)
        self.assertEqual(json.loads(cleaned), {"key": "value"})
        
    def test_markdown_no_lang(self):
        # Case 3: Markdown fences no lang
        raw = '```\n{"key": "value"}\n```'
        cleaned = clean_json_output(raw)
        self.assertEqual(json.loads(cleaned), {"key": "value"})
        
    def test_intro_text(self):
        # Case 4: Intro text
        raw = 'Here is the JSON:\n```json\n{"key": "value"}\n```'
        cleaned = clean_json_output(raw)
        self.assertEqual(json.loads(cleaned), {"key": "value"})
        
    def test_trailing_text(self):
        # Case 5: Trailing text
        raw = '```json\n{"key": "value"}\n```\nHope this helps!'
        cleaned = clean_json_output(raw)
        self.assertEqual(json.loads(cleaned), {"key": "value"})
        
    def test_mixed_text(self):
        # Case 6: Mixed
        raw = 'Sure, here is the data:\n\n{\n  "key": "value"\n}\n\nLet me know if you need edits.'
        cleaned = clean_json_output(raw)
        self.assertEqual(json.loads(cleaned), {"key": "value"})

    def test_list(self):
        # Case 7: List
        raw = '```json\n["item1", "item2"]\n```'
        cleaned = clean_json_output(raw)
        self.assertEqual(json.loads(cleaned), ["item1", "item2"])

if __name__ == '__main__':
    unittest.main()
