import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

student_data = pd.read_csv("student_data.csv")

students = student_data.iloc[0:38,:]

X = students.iloc[:,1:4]    # Features

Y = students.iloc[:,6:7]    # Target

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

prediction = model.predict(x_test)

accuracy = accuracy_score(prediction, y_test)

report = classification_report(prediction, y_test)

print("\nAccuracy = ", accuracy)
print("\nClassification report:\n", report)

def pre_model(aptitude: int, communication: int, coding: int):
    data = pd.DataFrame([[aptitude, communication, coding]])
    response = model.predict(data)
    return response