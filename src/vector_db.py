import chromadb
from sentence_transformers import SentenceTransformer
import json
import os

db_directory = "db"
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

client = chromadb.PersistentClient(path=db_directory)
collection = client.get_or_create_collection("real_estate_listings")

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

listings_file = os.path.join("data", "listings.json")
with open(listings_file, "r") as file:
    listings = json.load(file)

def store_listings_in_db(listings):
    ids = []
    embeddings = []
    metadatas = []
    documents = []

    for listing in listings:
        description = listing["listing"]
        embedding = embedding_model.encode(description).tolist()
        
        ids.append(listing["prompt"])
        embeddings.append(embedding)
        metadatas.append(listing)
        documents.append(description)

    collection.upsert(ids=ids, embeddings=embeddings, metadatas=metadatas, documents=documents)

store_listings_in_db(listings)
print("Listings and embeddings stored in ChromaDB.")

all_entries = collection.get()
print("Verification: All Stored Listings in Vector DB:")
for i, (document, metadata) in enumerate(zip(all_entries['documents'], all_entries['metadatas']), start=1):
    print(f"\nListing {i}:")
    print("Description:", document)
    print("Metadata:", metadata)