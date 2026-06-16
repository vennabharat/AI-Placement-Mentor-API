import numpy as np
import pandas as pd

students_original = pd.read_csv("student_placement_analysis.csv")

print(students_original.loc[len(students_original)-1:len(students_original), ["Aptitude", "Communication", "Coding"]].values)