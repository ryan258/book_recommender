# Book Recommender

This is a simple book recommendation system that uses OpenAI's GPT model to generate personalized book recommendations based on user preferences.

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/book-recommender.git
   cd book-recommender
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key to the file:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

## Usage

Run the main script:

```
python main.py
```

Follow the prompts to enter your book preferences and receive a recommendation.

## Running Tests

To run the tests:

```
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
