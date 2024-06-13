import unittest
from main import update_text_elements

class TestUpdateTextElements(unittest.TestCase):

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
        self.updated_texts = {
            "456": {"type": "headline", "text": "Welcome to our website", "new_text": "Welcome to the #1 Pizza Shop", "sectionName": "Hero"},
            "789": {"type": "paragraph", "text": "We offer the best services", "new_text": "The best pizza gordon ramsey didn't eat", "sectionName": "Hero"}
        }

    def test_update_text_elements(self):
        update_text_elements(self.sample_json, self.updated_texts)
        expected_json = {
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
                                "text": "Welcome to the #1 Pizza Shop"
                            }
                        },
                        {
                            "guid": "789",
                            "level": "widget",
                            "type": "paragraph",
                            "options": {
                                "text": "The best pizza gordon ramsey didn't eat"
                            }
                        }
                    ]
                }
            ]
        }
        self.assertEqual(self.sample_json, expected_json)

if __name__ == '__main__':
    unittest.main()
