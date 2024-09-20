import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

MODEL_NAME = "gpt-4o-mini"  # Updated to a more widely available model