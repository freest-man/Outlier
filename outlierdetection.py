# -*- coding: utf-8 -*-
"""OutlierDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17dteo-xwhCL9Lg9CevcHZa-po6BxM5VG
"""

import numpy as np
import matplotlib.pyplot as plt
from pyod.models.knn import KNN
from pyod.utils.data import generate_data
from pyod.utils.data import evaluate_print

# Generate some sample data (you can replace this with your dataset)
contamination = 0.1  # The proportion of outliers in the data
n_samples = 200
n_features = 2
X_train, X_test, y_train, y_test = generate_data(
    n_train=n_samples, n_test=n_samples, n_features=n_features, contamination=contamination)

# Initialize the KNN model
clf = KNN(contamination=contamination)

# Fit the model to the data
clf.fit(X_train)

# Predict outliers on the test set
y_test_pred = clf.predict(X_test)

# Get the outlier scores
outlier_scores = clf.decision_function(X_test)

# Plot the outliers
plt.figure(figsize=(10, 6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=outlier_scores, cmap='viridis')
plt.title('Outlier Detection with KNN')
plt.colorbar()
plt.show()