import numpy as np  # importing numarical python for array operations
import pandas as pd # importing pandas for data operationg

from sklearn.model_selection import train_test_split    # for splitting data into train & test for ML model
from sklearn.tree import DecisionTreeClassifier # for building ML classificaiton model
from sklearn.metrics import accuracy_score  # to calculate accuracy score of the model
from sklearn.metrics import classification_report   # to calculate precision, recall, f1-score

student_data = pd.read_csv("student_data.csv")  # creating data frame from csv data

students = student_data.iloc[0:38,:]    # selecting original data for model training

X = students.iloc[:,1:4]    # Feature selection

Y = students.iloc[:,6:7]    # Target variable

# splitting data into train & test data
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

model = DecisionTreeClassifier()    # ML classification model

model.fit(x_train, y_train) # model training

prediction = model.predict(x_test)  # making prediction with test data

accuracy = accuracy_score(prediction, y_test)   # calculating machine accuracy from test data

report = classification_report(prediction, y_test)  # calculating precision, recall, f1-score

print("\nAccuracy = ", accuracy)    
print("\nClassification report:\n", report)


# function for predicting student eligibility using ML model
def pre_model(aptitude: int, communication: int, coding: int):
    data = pd.DataFrame([[aptitude, communication, coding]])
    response = model.predict(data)
    return response