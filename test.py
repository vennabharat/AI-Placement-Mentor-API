import numpy as np 
import pandas as pd

students = pd.read_csv("student_placement_analysis.csv")

new = students.loc[len(students)-1:len(students), ["Aptitude", "Communication", "Coding"]].values

print(new[0][2])