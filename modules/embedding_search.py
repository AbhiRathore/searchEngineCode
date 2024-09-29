from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load a pre-trained sentence transformer model
def load_model():
    return SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Generate embeddings for the text content
def generate_embeddings(model, text):
    return model.encode(text)

# Build FAISS index
def build_faiss_index(embeddings):
    d = len(embeddings[0])  # Dimension of embeddings
    index = faiss.IndexFlatL2(d)
    index.add(np.array(embeddings))
    return index

# Search for k nearest neighbors
def search_faiss_index(index, query_embedding, k=5):
    D, I = index.search(np.array([query_embedding]), k)
    return I
