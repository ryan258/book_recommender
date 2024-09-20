# Book Recommender

This is a simple book recommendation system that uses OpenAI's GPT model to generate personalized book recommendations based on user preferences.

## Installation

1. Ensure you have Poetry installed. If not, install it by following the instructions [here](https://python-poetry.org/docs/#installation).

2. Clone this repository:

   ```
   git clone https://github.com/yourusername/book-recommender.git
   cd book-recommender
   ```

3. Install the project dependencies using Poetry:

   ```
   poetry install
   ```

4. Set up your OpenAI API key:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key to the file:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

## Usage

Activate the Poetry environment and run the main script:

```
poetry shell
python main.py
```

Alternatively, you can use the Poetry run command:

```
poetry run python main.py
```

Follow the prompts to enter your book preferences and receive a recommendation.

## Running Tests

To run the tests:

```
poetry run pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
