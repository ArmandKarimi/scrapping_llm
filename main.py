import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("GROQ_API_KEY")
print(f"GROQ API Key: {api_key}")
