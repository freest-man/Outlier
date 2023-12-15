# Outlier
Outlier Detection in PyOD and plotting
What is an Outlier?

An outlier is any data point that differs greatly from the rest of the observations in a dataset.

Outliers can impact the results of our analysis and statistical modeling drastically.

Real Life Example:

Usain Bolt’s record-breaking sprints are definitely outliers when you consider the majority of athletes.
In this example, we'll use the PYOD library with the K-Nearest Neighbors (KNN) algorithm for outlier detection and visualize the detected outliers.

PyOD provides access to around 20 outlier detection algorithms for detecting outliers in multivariate data.

![image](https://github.com/freest-man/Outlier/assets/116303271/bc3a137d-3362-43ea-bfc6-24ca5bd50056)


Import necessary libraries:

NumPy, matplotlib.pyplot, pyod.models.knn

The “generate_data” function creates a dataset with a specified proportion of outliers.

You can replace this with your actual dataset.

![image](https://github.com/freest-man/Outlier/assets/116303271/d8c7242c-4c80-4aee-9943-204ae6d828bb)


Initialize the KNN Model with the specified contamination (proportion of outliers).

Train the KNN model on the training data using the fit() method.

Use the predict() method to predict outliers in the test data.

![image](https://github.com/freest-man/Outlier/assets/116303271/47d47818-3a31-4b47-98de-7c8b158443a6)


The decision_function() method returns outlier scores for each data point.

Create a scatter plot to visualize the outliers.

Outlier scores determine the color of each point in the plot.


Remember outliers are not always bad!

But we need to detect them to understand their causes.
