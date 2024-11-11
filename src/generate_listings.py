import openai

def generate_listings():
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

    listings = []
    for prompt in prompts:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7
        )
        listing_text = response.choices[0].message['content'].strip()
        listings.append({
            "prompt": prompt,
            "listing": listing_text
        })
    return listings
