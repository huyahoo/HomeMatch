import chromadb
from models import embedding_model
import os

db_directory = "db"
client = chromadb.PersistentClient(path=db_directory)
collection = client.get_or_create_collection("real_estate_listings")

def is_database_populated():
    all_entries = collection.get()
    return len(all_entries.get('ids', [])) > 0

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
