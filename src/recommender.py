import openai
import json
from .models import BookRecommendation
from .config import OPENAI_API_KEY, MODEL_NAME

openai.api_key = OPENAI_API_KEY

def get_book_recommendation(user_preferences: str) -> BookRecommendation:
    try:
        response = openai.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a knowledgeable book recommendation system."},
                {"role": "user", "content": f"Based on these preferences, recommend a book: {user_preferences}"}
            ],
            functions=[{
                "name": "recommend_book",
                "description": "Recommend a book based on user preferences",
                "parameters": BookRecommendation.schema()
            }],
            function_call={"name": "recommend_book"}
        )

        recommendation_dict = json.loads(response.choices[0].message.function_call.arguments)
        return BookRecommendation(**recommendation_dict)
    except openai.error.OpenAIError as e:
        print(f"An error occurred while getting the book recommendation: {str(e)}")
        return None