import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI 

PROJECT_ROOT = Path(__file__).parent.parent

# Loading env variables from .env file
load_dotenv(dotenv_path=PROJECT_ROOT / ".env")

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL")

# Create the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Read the system prompt
prompt_path = PROJECT_ROOT / "prompts" / "tutor_prompts.txt"
system_prompt = prompt_path.read_text(encoding="utf-8")

# Define the user prompt
user_prompt = "Explain python lists using Data Science Example."

# Send the prompt to the model
response = client.responses.create(
    model=model,
    instructions = system_prompt,
    input = user_prompt
)

# Print the model's response
print(response.output_text)