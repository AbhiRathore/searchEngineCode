from modules.webCr import crawl_page, fetch_all
from modules.contentExtractor import extract_content_goose, extract_content_newspaper
from modules.userintent import init_classifier, extract_intent
from modules.embedding_search import load_model, generate_embeddings, build_faiss_index, search_faiss_index
from modules.ranking import rank_pages
from modules.feedback import update_ranking_based_on_feedback
from modules.cache import connect_redis, cache_results, get_cached_results
from modules.duckduckgosearch import *
import numpy as np
def main():
    # 1. Initialize components
    redis_conn = connect_redis()
    model = load_model()
    classifier = init_classifier()

    # 2. Crawling web content (synchronously)
    # url = "http://example.com"
    # html_content = crawl_page(url)
    
    # Optionally, crawl multiple pages asynchronously
    # urls = ["http://example1.com", "http://example2.com"]
    # html_contents = asyncio.run(fetch_all(urls))

    # 3. Extract content from the webpage

    user_query = "Find the best machine learning tutorials"

    urls = SearchCode(user_query)






    content = extract_content_goose(urls[0])

    # 4. Generate embeddings for the content
    content_embedding = generate_embeddings(model, content)

    # 5. Get user query and understand intent
    
    intent = extract_intent(classifier, user_query)
    print(f"User Intent: {intent}")

    # Generate embedding for query
    query_embedding = generate_embeddings(model, user_query)

    # 6. Check if the query is cached
    cached_results = get_cached_results(redis_conn, user_query)
    if cached_results is None:
        # For demonstration, assume you have more embeddings for other pages
        page_embeddings = [content_embedding]  # Replace with actual content embeddings

        # 7. Build FAISS index and search relevant content
        index = build_faiss_index(page_embeddings)
        ranked_indices = search_faiss_index(index, query_embedding)

        # 8. Cache the results
        cache_results(redis_conn, user_query, ranked_indices)
    else:
        ranked_indices = cached_results

    print(f"Ranked Results: {ranked_indices}")

    ranked_indices_list = ranked_indices[0]

    # 9. Simulate user feedback and update ranking
    user_clicks = [1, 0, 1,0,1]  # Simulate clicks
    dwell_times = [30, 20, 50,10,20]  # Simulate dwell times
    # updated_ranking = update_ranking_based_on_feedback(ranked_indices_list, user_clicks, dwell_times)

    # Page scores are initialized based on the order of ranked indices (e.g., 1st page = highest score)
    page_scores = np.array([len(urls) - i for i in ranked_indices[0]])

    # Get updated rankings based on feedback
    updated_scores = update_ranking_based_on_feedback(page_scores, user_clicks, dwell_times)

    # 10. Sort URLs based on updated rankings
    updated_indices = np.argsort(updated_scores)[::-1]
    updated_urls = [urls[i] for i in updated_indices]
    
    print(f"Updated Page Scores: {updated_scores}")
    print(f"Updated Ranked URLs: {updated_urls}")



    
    # print(f"Updated Ranking: {updated_ranking}")

if __name__ == "__main__":
    main()
