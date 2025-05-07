import numpy as np
import matplotlib.pyplot as plt

# Simulated structural data
# 0 = healthy, 1 = damaged
data = {
    'healthy': np.random.normal(0, 1, (50, 3)),
    'damaged': np.random.normal(2, 1, (50, 3))
}

# Combine and label
X = np.vstack((data['healthy'], data['damaged']))
y = np.array([0]*50 + [1]*50)

# Generate detectors randomly
def generate_detectors(n_detectors, feature_dim):
    return np.random.uniform(-1, 4, (n_detectors, feature_dim))

# Affinity function (Euclidean distance)
def affinity(detector, antigen):
    return np.linalg.norm(detector - antigen)

# Detection algorithm
def classify(detectors, threshold, test_sample):
    for detector in detectors:
        if affinity(detector, test_sample) < threshold:
            return 1  # Damaged
    return 0  # Healthy

# Generate detectors trained on healthy data (negative selection)
detectors = generate_detectors(100, X.shape[1])
threshold = 1.5

# Test classification accuracy
predictions = [classify(detectors, threshold, sample) for sample in X]
accuracy = np.mean(predictions == y)

print(f"Classification Accuracy: {accuracy * 100:.2f}%")

# Visualize the data
plt.figure(figsize=(10, 6))
plt.scatter(data['healthy'][:, 0], data['healthy'][:, 1], label='Healthy', alpha=0.5)
plt.scatter(data['damaged'][:, 0], data['damaged'][:, 1], label='Damaged', alpha=0.5)
plt.title('Structural Data Visualization')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid()
plt.show()

# Visualize the detectors
plt.figure(figsize=(10, 6))
plt.scatter(data['healthy'][:, 0], data['healthy'][:, 1], label='Healthy', alpha=0.5)
plt.scatter(data['damaged'][:, 0], data['damaged'][:, 1], label='Damaged', alpha=0.5)
plt.scatter(detectors[:, 0], detectors[:, 1], label='Detectors', color='red', alpha=0.5)
plt.title('Detectors Visualization')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid()
plt.show()

# Visualize the classification results
plt.figure(figsize=(10, 6))
plt.scatter(data['healthy'][:, 0], data['healthy'][:, 1], label='Healthy', alpha=0.5)
plt.scatter(data['damaged'][:, 0], data['damaged'][:, 1], label='Damaged', alpha=0.5)
predicted_labels = np.array(predictions)
plt.scatter(X[predicted_labels == 0][:, 0], X[predicted_labels == 0][:, 1], label='Predicted Healthy', color='green', alpha=0.5)
plt.scatter(X[predicted_labels == 1][:, 0], X[predicted_labels == 1][:, 1], label='Predicted Damaged', color='orange', alpha=0.5)
plt.title('Classification Results Visualization')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid()
plt.show()
