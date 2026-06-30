import os
from dotenv import load_dotenv
import google.generativeai as genai
 
load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
 
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="You are a concise assistant for engineers."
)
 
# --- Step 1: Basic call ---
# print("=== Basic Call ===")
# response = model.generate_content("Explain Docker in 2 sentences.")
# print(response.text)
# print(f"Tokens used: {response.usage_metadata}\n")
 
# --- Step 2: Temperature comparison ---
print("=== Temperature Comparison ===")
for temp in [0, 1]:
    config = genai.GenerationConfig(temperature=temp, max_output_tokens=100)
    response = model.generate_content(
        "Give me a creative name for a Python logging library.",
        generation_config=config
    )
    print(f"temp={temp}: {response.text.strip()}\n")
 
# --- Step 3: Streaming ---
# print("=== Streaming ===")
# response = model.generate_content(
#     "Write a haiku about Git.",
#     stream=True
# )
for chunk in response:
    print(chunk.text, end="", flush=True)
print()