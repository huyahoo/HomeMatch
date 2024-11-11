def get_buyer_preferences(interactive=True):
    questions = [
        "How big do you want your house to be?",
        "What are 3 most important things for you in choosing this property?",
        "Which amenities would you like?",
        "Which transportation options are important to you?",
        "How urban do you want your neighborhood to be?"
    ]

    if not interactive:
        answers = [
            "A comfortable three-bedroom house with a spacious kitchen and a cozy living room.",
            "A quiet neighborhood, good local schools, and convenient shopping options.",
            "A backyard for gardening, a two-car garage, and a modern, energy-efficient heating system.",
            "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.",
            "A balance between suburban tranquility and access to urban amenities like restaurants and theaters."
        ]
    else:
        answers = []
        for question in questions:
            answer = input(f"{question} ")
            answers.append(answer)

    preferences = {
        "house_size": answers[0],
        "important_factors": answers[1],
        "amenities": answers[2],
        "transportation": answers[3],
        "neighborhood_type": answers[4]
    }

    return preferences

if __name__ == "__main__":
    preferences = get_buyer_preferences(interactive=False)
    print("Collected Preferences:", preferences)
