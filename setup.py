from setuptools import setup, find_packages

setup(
    name="book_recommender",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai==0.27.0",
        "pydantic==1.10.7",
        "python-dotenv==1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "book-recommender=main:main",
        ],
    },
)