from datetime import datetime
import random

quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Believe you can and you're halfway there.",
    "Every day is a new opportunity to learn."
]

today = datetime.now().strftime("%Y-%m-%d")

print(f"Current Date: {today}")
print(f"Motivational Quote: {random.choice(quotes)}")
