import openai
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

openai.api_base = "https://openai.vocareum.com/v1"
openai.api_key = api_key

prompts = [
    "Generate a listing for a cozy two-bedroom apartment in a vibrant city neighborhood.",
    "Generate a listing for a luxury 5-bedroom home in an upscale suburban area.",
    "Generate a listing for a budget-friendly single-family home in a small town.",
    "Generate a listing for a modern studio apartment in the heart of downtown.",
    "Generate a listing for a large countryside property with lots of outdoor space.",
    "Generate a listing for a beach house with ocean views and outdoor amenities.",
    "Generate a listing for an eco-friendly 3-bedroom home in a sustainable community.",
    "Generate a listing for a high-end condo near a bustling shopping district.",
    "Generate a listing for a family-friendly home close to top-rated schools.",
    "Generate a listing for a small rustic cabin in the mountains."
]

def generate_listing(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print("An error occurred:", e)
        return "Error: API call failed."

listings = []
for prompt in prompts:
    listing_text = generate_listing(prompt)
    listings.append({
        "prompt": prompt,
        "listing": listing_text
    })
    
listings_file = "data/listings.json"
os.makedirs(os.path.dirname(listings_file), exist_ok=True)

if not os.path.exists(listings_file):
    with open(listings_file, "w") as file:
        json.dump([], file, indent=4)

with open(listings_file, "w") as file:
    json.dump(listings, file, indent=4)

print("10 diverse listings generated and saved.")
