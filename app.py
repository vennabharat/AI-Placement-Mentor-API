from pydantic import BaseModel #import BaseModel from pydantic_core
from fastapi import FastAPI # import FastAPI from fastapi

import pandas as pd #import pandas as pd

app = FastAPI() # create an instance of FastAPI

class Student(BaseModel):
    name: str
    aptitude: int
    communication: int
    coding: int
    
@app.post("/new_student") # create a POST endpoint at /new_student
def new_student(student: Student):
    student_data = pd.read_csv("student_data.csv") # read the student data from a csv file
    student = pd.DataFrame([student])
    student_data = pd.concat([student_data, student], ignore_index=True) # add the new student data to the existing student data
    student_data.to_csv("student_data.csv", index=False) # save the updated student data to the csv file    
    return(
        print("New student added successfully!")
    )