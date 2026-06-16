import numpy as np # importing numpy library for numerical operations
import pandas as pd # importing pandas library for data manipulation and analysis
import sklearn # importing scikit-learn library for machine learning algorithms
from sklearn.model_selection import train_test_split # importing train_test_split function for splitting the dataset into training and testing sets
from sklearn.tree import DecisionTreeClassifier # importing DecisionTreeClassifier for building a decision tree model
from sklearn.metrics import accuracy_score # importing accuracy_score for evaluating the performance of the model   
from sklearn.metrics import classification_report # importing classification_report for generating a report of the model's performance

students = pd.read_csv("student_placement_analysis.csv") # reading student data from a csv file

X = students[["Aptitude", "Communication", "Coding"]] # selecting the features for the model
y = students["Placement_Status"] # selecting the target variable for the model

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # splitting the dataset into training and testing sets

model = DecisionTreeClassifier() # creating an instance of the DecisionTreeClassifier

model.fit(X_train, y_train) # fitting the model to the training data

y_pred = model.predict(X_test) # making predictions on the test set

accuracy = accuracy_score(y_test, y_pred) # calculating the accuracy of the model

report = classification_report(y_test, y_pred) # generating a classification report

print("\nModel Accuracy:", accuracy) # printing the accuracy of the model

print("\nClassification Report:\n", report) # printing the classification report

prediction = model.predict(students[:-1,:])

print(prediction)