import numpy as np  # importing numpy library for numerical operations
import pandas as pd # importing pandas library for data manipulation and analysis

students = pd.read_csv("student_data.csv") # reading student data from a csv file

average_aptitude = students["Aptitude"].mean()  # calculate the average aptitude score
average_communication = students["Communication"].mean()    # calculate the average communication score
average_coding = students["Coding"].mean()  # calculate the average coding score

t_students = students   # create a copy of the original students DataFrame

t_students["Total"] = t_students["Aptitude"] + t_students["Communication"] + t_students["Coding"]  # calculate the total score for each student
t_students["Average"] = t_students["Total"] / 3  # calculate the average score for each student

top_performer = t_students.loc[t_students["Total"].idxmax()]  # find the student with the highest total score

lowest_performer = t_students.loc[t_students["Total"].idxmin()]  # find the student with the lowest total score

# Printing the report

print("Average Aptitude Score:", round(average_aptitude, 2))
print("Average Communication Score:", round(average_communication, 2))
print("Average Coding Score:", round(average_coding, 2))
print("\nTop Performer:")
print(top_performer["Student"], "with a total score of", round(top_performer["Total"], 2))
print("\nLowest Performer:")
print(lowest_performer["Student"], "with a total score of", round(lowest_performer["Total"], 2))