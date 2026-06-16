import numpy as np  # importing numpy library for numerical operations
import pandas as pd # importing pandas library for data manipulation
import sklearn # importing scikit-learn library for machine learning algorithms
from sklearn.model_selection import train_test_split # importing train_test_split function for splitting the dataset into training and testing sets
from sklearn.tree import DecisionTreeClassifier # importing DecisionTreeClassifier for building a decision tree model
from fastapi import FastAPI # importing FastAPI for creating the API
from pydantic import BaseModel # importing BaseModel from pydantic for data validation  
app = FastAPI() # creating an instance of FastAPI

class Student(BaseModel):
    Student: str
    Aptitude: int
    Communication: int
    Coding: int
    