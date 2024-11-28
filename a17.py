# Confusion Matrix values
TP = 1  # True Positives
FP = 1  # False Positives
FN = 8  # False Negatives
TN = 90  # True Negatives

# Calculations
total = TP + FP + FN + TN

# Accuracy
accuracy = (TP + TN) / total

# Error Rate
error_rate = (FP + FN) / total

# Precision
precision = TP / (TP + FP) if (TP + FP) != 0 else 0

# Recall
recall = TP / (TP + FN) if (TP + FN) != 0 else 0

# Print the results
print(f"Accuracy: {accuracy:.2f}")
print(f"Error Rate: {error_rate:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
