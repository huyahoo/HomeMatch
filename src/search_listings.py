from sentence_transformers import SentenceTransformer
import chromadb
from user_preferences import get_buyer_preferences

db_directory = "db"

client = chromadb.PersistentClient(path=db_directory)
collection = client.get_or_create_collection("real_estate_listings")

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def search_listings(preferences):
    preference_text = (
        f"House Size: {preferences['house_size']}. "
        f"Important Factors: {preferences['important_factors']}. "
        f"Amenities: {preferences['amenities']}. "
        f"Transportation: {preferences['transportation']}. "
        f"Neighborhood Type: {preferences['neighborhood_type']}."
    )

    preference_embedding = embedding_model.encode(preference_text).tolist()

    results = collection.query(
        query_embeddings=[preference_embedding],
        n_results=5,
        include=["documents", "metadatas"]
    )

    return results

if __name__ == "__main__":
    preferences = get_buyer_preferences(interactive=False)

    search_results = search_listings(preferences)

    print("Top Matching Listings:")
    for i, (document, metadata) in enumerate(zip(search_results['documents'], search_results['metadatas']), start=1):
        print(f"\nListing {i}:")
        print("Description:", document)
        print("Metadata:", metadata)