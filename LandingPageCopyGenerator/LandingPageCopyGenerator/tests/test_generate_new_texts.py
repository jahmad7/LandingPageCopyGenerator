import unittest
from unittest.mock import patch, MagicMock
from main import generate_new_texts

class TestGenerateNewTexts(unittest.TestCase):

    def setUp(self):
        self.text_elements = {
            "456": {"type": "headline", "text": "Welcome to our website", "sectionName": "Hero"},
            "789": {"type": "paragraph", "text": "We offer the best services", "sectionName": "Hero"}
        }
        self.context = "Awesome Company: Doing Awesome Things and Providing Awesome Services."

    @patch('main.OpenAI')
    def test_generate_new_texts(self, MockOpenAI):
        mock_client = MockOpenAI.return_value
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = 'New Headline'
        mock_client.chat.completions.create.return_value = mock_response

        new_texts = generate_new_texts(self.text_elements, self.context)
        self.assertEqual(new_texts["456"]["new_text"], "New Headline")

if __name__ == '__main__':
    unittest.main()
