from textstat import textstat

def get_readability_score(text):
    return textstat.flesch_reading_ease(text)

# Rank pages by readability score
readability_scores = [get_readability_score(text) for text in webpage_texts]
ranked_by_readability = np.argsort(readability_scores)[::-1]
print(ranked_by_readability)
