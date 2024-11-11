import openai

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
        max_tokens=300,
        temperature=0.7
    )

    return response.choices[0].message['content'].strip()
