from pydantic import BaseModel, Field
from typing import List

class BookRecommendation(BaseModel):
    title: str = Field(..., description="The title of the recommended book")
    author: str = Field(..., description="The author of the recommended book")
    genre: str = Field(..., description="The primary genre of the book")
    publication_year: int = Field(..., description="The year the book was published")
    summary: str = Field(..., description="A brief summary of the book's plot or content")
    reasons: List[str] = Field(..., description="List of reasons why this book is recommended")