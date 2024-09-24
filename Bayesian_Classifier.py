import pandas as pd
import numpy as np
from collections import defaultdict
from random import shuffle

# Load the dataset
dataset = pd.read_csv('Iris_dataset/iris.data', header=None)
dataset.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Split the dataset into features and target variable
X = dataset.drop('class', axis=1).values
y = dataset['class'].values


# Manually split the dataset into training and testing sets
def train_test_split(X, y, test_size=0.2):
    indices = list(range(len(X)))
    shuffle(indices)
    split_idx = int(len(X) * (1 - test_size))
    train_indices = indices[:split_idx]
    test_indices = indices[split_idx:]
    X_train = X[train_indices]
    y_train = y[train_indices]
    X_test = X[test_indices]
    y_test = y[test_indices]
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Calculate the prior probabilities for each class
classes, class_counts = np.unique(y_train, return_counts=True)
priors = class_counts / y_train.shape[0]

# Calculate the mean and variance for each feature per class
means = np.zeros((len(classes), X_train.shape[1]))
variances = np.zeros((len(classes), X_train.shape[1]))

for idx, cls in enumerate(classes):
    X_cls = X_train[y_train == cls]
    means[idx, :] = X_cls.mean(axis=0)
    variances[idx, :] = X_cls.var(axis=0)


# Define the Gaussian probability density function
def gaussian_pdf(x, mean, var):
    return (1 / np.sqrt(2 * np.pi * var)) * np.exp(- (x - mean) ** 2 / (2 * var))


# Make predictions
def predict(X):
    posteriors = []
    for x in X:
        class_posteriors = []
        for idx, cls in enumerate(classes):
            prior = np.log(priors[idx])
            likelihood = np.sum(np.log(gaussian_pdf(x, means[idx], variances[idx])))
            posterior = prior + likelihood
            class_posteriors.append(posterior)
        posteriors.append(classes[np.argmax(class_posteriors)])
    return posteriors


# Predict on the testing set
y_pred = predict(X_test)


# Calculate accuracy score and print correct/incorrect classifications
def evaluate_classifier(y_true, y_pred):
    correct_counts = defaultdict(int)
    incorrect_counts = defaultdict(int)

    for true, pred in zip(y_true, y_pred):
        if true == pred:
            correct_counts[true] += 1
        else:
            incorrect_counts[true] += 1

    for cls in classes:
        print(f"Class {cls}: Correctly classified: {correct_counts[cls]}, Incorrectly classified: {incorrect_counts[cls]}")


# Evaluate the classifier
evaluate_classifier(y_test, y_pred)
