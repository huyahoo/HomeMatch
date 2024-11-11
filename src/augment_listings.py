import openai
import os
from dotenv import load_dotenv
from user_preferences import get_buyer_preferences
from search_listings import search_listings

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

openai.api_base = "https://openai.vocareum.com/v1"
openai.api_key = api_key

def personalize_description(description, preferences):
    messages = [
        {"role": "system", "content": "You are an assistant that personalizes real estate listings based on buyer preferences."},
        {"role": "user", "content": (
            f"Buyer preferences: {preferences}. "
            f"Original Listing Description: {description}. "
            "Rewrite the description to highlight aspects that align with the buyer's preferences while keeping all factual information intact."
        )}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,
        temperature=0.7
    )

    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    preferences = get_buyer_preferences(interactive=False)
    search_results = search_listings(preferences)

    print("Personalized Listings:")
    for i, (description, metadata) in enumerate(zip(search_results['documents'], search_results['metadatas']), start=1):
        original_description = description[0] if isinstance(description, list) else description
        personalized_description = personalize_description(original_description, preferences)

        print(f"\nListing {i}:")
        print("Original Description:", original_description)
        print("Personalized Description:", personalized_description)
        print("Metadata:", metadata)