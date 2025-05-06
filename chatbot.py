import os  # For environment variables
import time   # For simulating typing effect
import concurrent.futures  # Multi-threading for faster execution
import nltk  # Automatic sentiment analysis
from nltk.sentiment import SentimentIntensityAnalyzer  # VADER sentiment analysis
from nltk import download  # For downloading NLTK resources
from google import genai   # Google Gemini AI client library
from google.genai import types  # Types for content generation
from dotenv import load_dotenv  # For loading environment variables

# Load environment variables for security
load_dotenv()

# Set up API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("**Error: GEMINI_API_KEY is not set. Please check your .env file.**")

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Multi-threaded execution setup
executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

def simulate_typing(text, delay=0.005):
    """Simulates typing effect for a more natural chatbot experience."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def format_ai_reply(text):
    """Formats AI response for better readability by adding bullet points."""
    return text.replace(". ", ".\n- ")

def analyze_sentiment(user_input):
    """Detects user sentiment and returns a mood-based response prefix."""
    score = analyzer.polarity_scores(user_input)["compound"]
    if score > 0.3:
        return "😊"
    elif score < -0.3:
        return "😟"
    else:
        return "😐"

def generate():
    """Main chatbot loop for handling user interactions."""
    client = genai.Client(api_key=GEMINI_API_KEY)
    model = "gemini-2.0-flash"

    print("\n🤖 Bot: Welcome to the Healthcare Chatbot! Type 'commands' for help.\n")
    
    while True:
        try:
            user_input = input("👤 You: ").strip().lower()

            # Exit condition
            if user_input == "exit" or user_input == "quit" or user_input == "bye":
                simulate_typing("🤖 Bot: Goodbye! Take care. 😊")
                break
            
            # Help & commands instructions
            if user_input in ["help", "how to exit", "exit instructions", "commands"]:
                simulate_typing("🤖 Bot: Available commands:\n  - 'exit' → Quit chatbot\n  - 'help' → View instructions\n  - 'commands' → See available options\n")
                continue
            
            # Detect sentiment
            sentiment_emoji = analyze_sentiment(user_input)

            # Prepare user input as content for the AI model
            contents = [types.Part.from_text(text=user_input)]

            # Generate response with a healthcare focus
            generate_content_config = types.GenerateContentConfig(
                temperature=0.5,
                response_mime_type="text/plain",
                system_instruction=[
                    types.Part.from_text(text="""You are a healthcare chatbot designed to provide preliminary medical guidance to users seeking quick information when professional help is unavailable. Your primary goal is to analyze user inquiries, deliver accurate health advice based on verified medical sources, and ensure ethical compliance. Your role is advisory only—you do not replace professional medical consultations but instead guide users toward appropriate healthcare services when necessary. Maintain a conversational tone, avoid overly technical jargon, and prioritize user understanding and comfort."""),    
                ],
            )

            # Stream response asynchronously using multi-threading
            future = executor.submit(
                client.models.generate_content_stream,
                model=model,
                contents=contents,
                config=generate_content_config,
            )

            print(f"{sentiment_emoji} 🤖 Bot: ", end="")  # Prefix sentiment before response
            for chunk in future.result():
                simulate_typing(format_ai_reply(chunk.text))  # Format response for readability

        except Exception as e:
            simulate_typing(f"Bot: **An error occurred: {e}**")  # Handle exceptions gracefully

if __name__ == "__main__":
    generate()