from sklearn.metrics import precision_score, recall_score
import numpy as np

# Example relevance labels and predictions
true_labels = [1, 1, 0, 1, 0]
predicted_labels = [1, 0, 1, 1, 0]

precision = precision_score(true_labels, predicted_labels)
recall = recall_score(true_labels, predicted_labels)
print(f"Precision: {precision}, Recall: {recall}")
