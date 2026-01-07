# Gemini RAG Chatbot

This project implements a chatbot using Google's Gemini API and ChromaDB for Retrieval-Augmented Generation (RAG). It allows users to ask questions and get answers based on a specific knowledge base (e.g., Operating Systems or WW2 history).

## Features
- **RAG Architecture**: Uses ChromaDB to store and retrieve relevant context.
- **Gemini Integration**: Utilizes Google's Gemini models for embedding generation and answer synthesis.
- **Web Interface**: A Flask-based web application to interact with the bot.
- **Console Mode**: Standalone scripts to run the bot in the terminal.

## Prerequisites
- Python 3.8 or higher
- A Google Cloud Project with the Gemini API enabled
- An API Key for Google Gemini

## Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd try-gemini
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

You need to configure your Google API Key.
Open `os_bot.py` (for the OS bot) or `main.py` (for the WW2 bot) and replace the placeholder API key with your own:

```python
GOOGLE_API_KEY = "YOUR_ACTUAL_API_KEY_HERE"
```

> **Note**: For better security, consider using environment variables instead of hardcoding API keys.

## Running the Application

### Web Interface (Flask)
To run the web application which uses the OS Bot:

1.  Run the Flask app:
    ```bash
    python app.py
    ```
2.  Open your browser and navigate to: `http://127.0.0.1:5000`

### Console Mode
You can also run the bots directly in your terminal:

**Operating Systems Bot:**
```bash
python os_bot.py
```

**WW2 History Bot:**
```bash
python main.py
```

## Project Structure
- `app.py`: Flask application server.
- `os_bot.py`: Logic for the Operating Systems bot (RAG + Gemini).
- `main.py`: Logic for the WW2 history bot.
- `requirements.txt`: Python dependencies.
- `templates/`: HTML templates for the web interface.
