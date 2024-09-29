import numpy as np

# Update rankings based on user behavior (clicks, dwell times)
def update_ranking_based_on_feedback(page_scores, user_clicks, dwell_times):
    # Convert lists to NumPy arrays for element-wise operations
    print(f"ranked_indices_list is {page_scores}")
    print(f"ranked_indices_list len is  {len(page_scores)}")
    user_clicks = np.array(user_clicks)
    dwell_times = np.array(dwell_times)

    print(len(user_clicks))
    print(len(page_scores))
    print(len(dwell_times))

    # Ensure both arrays have the same length as page_scores
    if len(user_clicks) != len(page_scores) or len(dwell_times) != len(page_scores):
        raise ValueError("The length of user_clicks and dwell_times must match the length of page_scores.")


    feedback_weights = user_clicks * 0.7 + dwell_times * 0.3
    return page_scores + feedback_weights
