def get_buyer_preferences(interactive=True):
    if interactive:
        print("\nPlease enter your preferences for your ideal home.")
        house_size = input("1. How big do you want your house to be? ")
        important_factors = input("2. What are the 3 most important things for you in choosing this property? ")
        amenities = input("3. Which amenities would you like? ")
        transportation = input("4. Which transportation options are important to you? ")
        neighborhood_type = input("5. How urban do you want your neighborhood to be? ")

    preferences = {
        "house_size": house_size,
        "important_factors": important_factors,
        "amenities": amenities,
        "transportation": transportation,
        "neighborhood_type": neighborhood_type
    }

    return preferences
