import chromadb
from models import embedding_model

db_directory = "db"
client = chromadb.PersistentClient(path=db_directory)
collection = client.get_or_create_collection("real_estate_listings")

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
        n_results=3,
        include=["documents", "metadatas"]
    )

    return results
