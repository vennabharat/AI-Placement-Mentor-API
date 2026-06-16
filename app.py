from fastapi import FastAPI 
from pydantic import BaseModel
from evaluation import evaluate # custom library
from prediction_model import pre_model  # custom library
from google import genai
from dotenv import load_dotenv
import os
import numpy as np
import pandas as pd

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

app = FastAPI()

data = pd.DataFrame()

student_data = pd.read_csv("student_data.csv")

client = genai.Client(api_key=api_key)

class Student(BaseModel):
    name: str
    aptitude: int 
    communication: int 
    coding: int 

@app.post("/new_student")
def new_student(new_student: Student):
    total, average = evaluate(new_student.aptitude, new_student.communication, new_student.coding)
    student = pd.DataFrame([
        {
            "Student" : new_student.name, 
            "Aptitude" : new_student.aptitude,
            "Communication" : new_student.communication,
            "Coding" : new_student.coding, 
            "Total" : round(total, 2),
            "Average" : round(average, 2), 
            "Placement_Status" : pre_model(
                new_student.aptitude, 
                new_student.communication,
                new_student.coding
            )[0]
        }
    ])

    student_data.loc[len(student_data)] = student.iloc[0]   #Adding new student to database
    student_data.to_csv("student_data.csv", index=False)
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=f"""
            Your a placement mentor, analyse student score in each subject and suggest
            practical & acheivable solution.
            Aptitude: {new_student.aptitude}
            Communication: {new_student.communication}
            Coding: {new_student.coding}
        """
    )
    
    return {
        "Student Name" : new_student.name, 
        "Aptitude" : new_student.aptitude, 
        "Communication" : new_student.communication, 
        "Coding" : new_student.coding, 
        "Placement_Status" : student["Placement_Status"],
        "Mentor advice" : response.text
    }