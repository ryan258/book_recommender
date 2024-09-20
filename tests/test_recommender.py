import pytest
from unittest.mock import patch, MagicMock
from book_recommender.recommender import get_book_recommendation
from book_recommender.models import BookRecommendation

@patch('book_recommender.recommender.OpenAI')
def test_get_book_recommendation(mock_openai):
    mock_client = MagicMock()
    mock_openai.return_value = mock_client
    mock_client.chat.completions.create.return_value.choices[0].message.function_call.arguments = '''
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
    
    assert isinstance(result, BookRecommendation)
    assert result.title == "The Time Machine"
    assert result.author == "H.G. Wells"