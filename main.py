import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("GROQ_API_KEY")
db_url = os.getenv("DATABASE_URL")

print(f"GROQ API Key: {api_key}")
print(f"Database URL: {db_url}")

# import pandas
