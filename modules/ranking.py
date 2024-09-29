from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Rank pages based on cosine similarity
def rank_pages(query_embedding, page_embeddings):
    similarity_scores = cosine_similarity([query_embedding], page_embeddings)[0]
    return np.argsort(similarity_scores)[::-1]
