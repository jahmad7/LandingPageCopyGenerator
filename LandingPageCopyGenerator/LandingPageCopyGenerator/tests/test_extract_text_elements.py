import unittest
from main import extract_text_elements

class TestExtractTextElements(unittest.TestCase):

    def setUp(self):
        self.sample_json = {
            "boxes": [
                {
                    "guid": "123",
                    "level": "section",
                    "name": "Hero",
                    "boxes": [
                        {
                            "guid": "456",
                            "level": "widget",
                            "type": "headline",
                            "options": {
                                "text": "Welcome to our website"
                            }
                        },
                        {
                            "guid": "789",
                            "level": "widget",
                            "type": "paragraph",
                            "options": {
                                "text": "We offer the best services"
                            }
                        }
                    ]
                }
            ]
        }

    def test_extract_text_elements(self):
        expected = {
            "456": {"type": "headline", "text": "Welcome to our website", "sectionName": "Hero"},
            "789": {"type": "paragraph", "text": "We offer the best services", "sectionName": "Hero"}
        }
        result = extract_text_elements(self.sample_json)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()