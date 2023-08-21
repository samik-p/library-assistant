import os

import openai
from dotenv import load_dotenv

load_dotenv()

# authenticate
openai.api_key = os.getenv("OPENAI_API_KEY")
