import unittest
from unittest.mock import patch, mock_open
from main import main

class TestMainFunction(unittest.TestCase):

    @patch('main.extract_text_elements')
    @patch('main.generate_new_texts')
    @patch('main.update_text_elements')
    @patch('builtins.open', new_callable=mock_open, read_data='{"boxes": []}')
    @patch('main.json.dump')
    def test_main(self, mock_json_dump, mock_open, mock_update, mock_generate, mock_extract):
        sample_text_elements = {
            "456": {"type": "headline", "text": "Welcome to our website", "sectionName": "Hero"},
            "789": {"type": "paragraph", "text": "We offer the best services", "sectionName": "Hero"}
        }
        sample_json = {
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

        mock_extract.return_value = sample_text_elements
        mock_generate.return_value = sample_text_elements
        mock_update.return_value = sample_json

        # Mock the sys.argv to pass the correct arguments
        with patch('sys.argv', ['main.py', 'input.json', 'output.json', 'Test Context']):
            main()

        # Check that both files are opened and written to
        expected_calls = [
            unittest.mock.call('results/output.json', 'w'),
            unittest.mock.call('results/extraction_output.json', 'w')
        ]
        mock_open.assert_has_calls(expected_calls, any_order=True)
        mock_json_dump.assert_called()

if __name__ == '__main__':
    unittest.main()
