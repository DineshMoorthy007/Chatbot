# Healthcare Chatbot 🤖

An intelligent, sentiment-aware chatbot designed to provide preliminary healthcare guidance when professional medical assistance is unavailable.

## 🌟 Key Features
- **Sentiment Analysis**: Understands user emotions using VADER sentiment analysis.
- **AI-Powered Responses**: Leverages Google Gemini AI for accurate and context-aware healthcare guidance.
- **Secure Configuration**: Protects sensitive data by securely loading API keys from a `.env` file.
- **High Performance**: Implements multi-threading for faster response times.
- **Natural Interaction**: Simulates typing for a more human-like chatbot experience.

## 🛠️ Installation Guide
### Prerequisites
Ensure the following are installed on your system:
- Python 3.8 or higher
- Google Gemini AI SDK
- `nltk` (for sentiment analysis)
- `python-dotenv` (for managing environment variables)

### Setup Instructions
1. **Clone the Repository**:
    ```sh
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure API Keys**:
    - Create a `.env` file in the project root.
    - Add your Google Gemini API key:
      ```env
      GEMINI_API_KEY=your_api_key_here
      ```

4. **Download VADER Lexicon**:
    - Run the following command in your terminal:
      ```sh
      python -m nltk.downloader vader_lexicon
      ```
    - Alternatively, include this in your code temporarily and execute it:
      ```python
      import nltk
      nltk.download("vader_lexicon")
      ```

### 🚀 Usage
Start the chatbot by running:
```sh
python chatbot.py
```

### 💬 Available Commands
- `exit` → Quit the chatbot.
- `help` → Display usage instructions.
- `commands` → List all available commands.

## ⚠️ Limitations
- **Not a Replacement for Medical Advice**: Always consult a healthcare professional for serious concerns.
- **Internet Dependency**: Requires an active internet connection for AI-powered responses.

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

Enjoy using the Healthcare Chatbot! 😊🚀
