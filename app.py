from pydantic import BaseModel #import BaseModel from pydantic_core
from fastapi import FastAPI # import FastAPI from fastapi

import pandas as pd #import pandas as pd

app = FastAPI() # create an instance of FastAPI

class Student(BaseModel):
    Student: str
    Aptitude: int
    Communication: int
    Coding: int

@app.post("/add_student/") # define a POST endpoint to add a student
def add_student(student: Student):
    students = pd.read_csv("student_placement_analysis.csv") # read the existing student data from a csv file
    new_student = pd.DataFrame([student.model_dump()]) # create a new DataFrame for the new student
    new_student["id"] = len(students) + 1 # assign a new id to the new student
    new_student["Total"] = new_student["Aptitude"] + new_student["Communication"] + new_student["Coding"] # calculate the total score for the new student
    new_student["Average"] = new_student["Total"] / 3 # calculate the average score for the new student
    new_student["Placement_Status"] = any # determine the placement status based on average score
    students.loc[len(students)] = new_student.iloc[0] # add the new student to the existing DataFrame
    students.to_csv("student_placement_analysis.csv", index=False) # save the updated student data back to the csv file
    return {"message": "Student added successfully"} # return a success message
