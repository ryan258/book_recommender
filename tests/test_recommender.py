import unittest
from unittest.mock import patch
from src.recommender import get_book_recommendation
from src.models import BookRecommendation

class TestRecommender(unittest.TestCase):
    @patch('src.recommender.openai.chat.completions.create')
    def test_get_book_recommendation(self, mock_create):
        mock_create.return_value.choices[0].message.function_call.arguments = '''
        {
            "title": "The Time Machine",
            "author": "H.G. Wells",
            "genre": "Science Fiction",
            "publication_year": 1895,
            "summary": "A scientist invents a time machine and travels to the future, encountering two post-human races.",
            "reasons": ["Classic science fiction novel", "Explores themes of time travel", "Philosophical undertones"]
        }
        '''

        result = get_book_recommendation("I like science fiction with time travel")
        
        self.assertIsInstance(result, BookRecommendation)
        self.assertEqual(result.title, "The Time Machine")
        self.assertEqual(result.author, "H.G. Wells")

if __name__ == '__main__':
    unittest.main()