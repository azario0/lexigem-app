# LexiGem 💎

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

LexiGem is a beautiful and simple web application that acts as an AI-powered lexicographer. Using Google's Gemini API, it provides complete, dictionary-style entries for words in multiple languages, starting with English and French.

## Features

- **AI-Powered Definitions**: Leverages the power of the Google Gemini 1.5 Flash model for comprehensive and accurate results.
- **Multilingual Support**: Provides dictionary entries in both English and French.
- **Detailed Entries**: Generates pronunciation (IPA), part of speech, definitions, synonyms, antonyms, example sentences, and etymology.
- **Clean & Responsive UI**: Built with Bootstrap 5 for a seamless experience on both desktop and mobile devices.
- **Secure API Key Handling**: Uses a `.env` file to keep your API key safe and out of the source code.
- **Easy to Set Up**: Get up and running in just a few simple steps.

## Tech Stack

- **Backend**: Python 3, Flask
- **AI Model**: Google Gemini API (`gemini-1.5-flash`)
- **Frontend**: HTML, Bootstrap 5
- **Dependencies**:
  - `google-generativeai`
  - `Flask`
  - `python-dotenv`
  - `Markdown`

## Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

- Python 3.8 or higher
- A Google Gemini API Key. You can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/azario0/LexiGem.git
    cd LexiGem
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure your API Key:**
    - Create a new file in the root directory named `.env`.
    - Add your Google API key to this file:
      ```
      GOOGLE_API_KEY="YOUR_API_KEY_HERE"
      ```

### Running the Application

Once the setup is complete, run the Flask application from the root directory:

```sh
flask run
```

Open your web browser and navigate to `http://127.0.0.1:5000` to start using LexiGem!

## Project Structure

```
LexiGem/
├── .env                  # Stores your secret API key
├── app.py                # The main Flask application logic
├── requirements.txt      # Project dependencies
├── LICENSE               # Project license
└── templates/
    └── index.html        # The HTML template for the user interface
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
_This project was created by azario0 and is powered by Google Gemini._
