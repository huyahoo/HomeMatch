# main.py

import os
import openai
from dotenv import load_dotenv

from generate_listings import generate_listings
from vector_db import store_listings_in_db, is_database_populated
from user_preferences import get_buyer_preferences
from search_listings import search_listings
from augment_listings import personalize_description

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

openai.api_base = "https://openai.vocareum.com/v1"
openai.api_key = api_key


# Suppress tokenizers parallelism warning
# os.environ["TOKENIZERS_PARALLELISM"] = "false"

def main():
    if not is_database_populated():
        print("Retrieving listings ...")
        
        listings = generate_listings()

        store_listings_in_db(listings)
        print("Updating ...")
    else:
        print("HomeMatch are Ready.")
        
    print("Welcome to HomeMatch!")

    while True:
        preferences = get_buyer_preferences(interactive=True)

        search_results = search_listings(preferences)
        
        print("Searching ...")

        if not search_results['documents']:
            print("\nNo matching listings found based on your preferences.")
        else:
            print("\nPersonalized Listings:")
            for i, (document, metadata) in enumerate(zip(search_results['documents'], search_results['metadatas']), start=1):
                original_description = document[0] if isinstance(document, list) else document
                personalized_description = personalize_description(original_description, preferences)

                print(f"\nListing {i}:")
                print("Original Description:\n", original_description)
                print("\nPersonalized Description:\n", personalized_description)
                print("\n----------------------------------------")

        continue_choice = input("\nWould you like to search with different preferences? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Thank you for using HomeMatch! Goodbye!")
            break

if __name__ == "__main__":
    main()
