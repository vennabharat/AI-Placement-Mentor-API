from fastapi import FastAPI # importing fastapi for web operationg
from pydantic import BaseModel  # for data validation
from evaluation import evaluate # custom library for total & average 
from prediction_model import pre_model  # custom library for student placement eligibility prediction
from google import genai    # importing genai from google for LLM integration
from dotenv import load_dotenv  # dot env fot securing API key
import os
import numpy as np  # numerical python for array operations
import pandas as pd # pandas for data operations

load_dotenv()   # loading dot env for calling secured API key

api_key = os.getenv("GEMINI_API_KEY")   # calling api key

app = FastAPI() # creating fastapi for endpoints

data = pd.DataFrame()   # new dataframe for saving data

student_data = pd.read_csv("student_data.csv")  # creating dataframe from csv data

client = genai.Client(api_key=api_key)  # calling LLM using API key

class Student(BaseModel):   # new class as datatype for passing values to endpoints
    name: str
    aptitude: int 
    communication: int 
    coding: int 

# endpoint for creating new student & LLM advice
@app.post("/new_student")
def new_student(new_student: Student):

    # calculating total & average from endpoint parameters using custom function - evaluate
    total, average = evaluate(new_student.aptitude, new_student.communication, new_student.coding)
    # creating new data frame from student data
    student = pd.DataFrame([
        {
            "Student" : new_student.name, 
            "Aptitude" : new_student.aptitude,
            "Communication" : new_student.communication,
            "Coding" : new_student.coding, 
            "Total" : round(total, 2),
            "Average" : round(average, 2), 
            # calling ML classification model for student placement eligibility prediction
            "Placement_Status" : pre_model(
                new_student.aptitude, 
                new_student.communication,
                new_student.coding
            )[0]
        }
    ])

    student_data.loc[len(student_data)] = student.iloc[0]   # Adding new student to database
    student_data.to_csv("student_data.csv", index=False)    # saving new data to database
    
    # calling LLM for student preparation advice
    response = client.models.generate_content(
        model="gemini-2.5-flash",   # using gemini 2.5 flas LLM model
        
        # passing data to LLM for response with student scores
        contents=f"""
            Your a placement mentor, analyse student score in each subject and suggest
            practical & acheivable solution.
            Aptitude: {new_student.aptitude}
            Communication: {new_student.communication}
            Coding: {new_student.coding}
        """
    )
    # returning required student data
    return {
        "Student Name" : new_student.name, 
        "Aptitude" : new_student.aptitude, 
        "Communication" : new_student.communication, 
        "Coding" : new_student.coding, 
        "Placement_Status" : student["Placement_Status"],
        "Mentor advice" : response.text
    }