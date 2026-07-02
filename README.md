# tweetgen
A simple Langchain based app that generates tweets on a desired topic.

## Running the app

Requires [uv](https://docs.astral.sh/uv/).

1. Install dependencies:
   ```bash
   uv sync
   ```
2. Create a `.env` file with your Google Gemini API key:
   ```
   GOOGLE_API_KEY=your-key-here
   ```
3. Launch the app:
   ```bash
   uv run streamlit run main.py
   ```
   It opens at http://localhost:8501.
