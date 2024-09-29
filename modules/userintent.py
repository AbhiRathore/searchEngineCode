from transformers import pipeline

# Initialize BERT-based sentiment analysis pipeline
def init_classifier():
    return pipeline('sentiment-analysis')

# Perform intent extraction (example using sentiment analysis)
def extract_intent(classifier, user_query):
    return classifier(user_query)
