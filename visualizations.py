import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("student_data.csv") # read the student data from a csv file

temp_students = students.copy() # create a copy of the original students DataFrame

temp_students["Total"] = temp_students["Aptitude"] + temp_students["Communication"] + temp_students["Coding"] # calculate the total score for each student

# Plotting student performance
plt.figure(figsize=(10, 6)) # set the figure size
plt.bar(temp_students["Student"], temp_students["Total"], color='skyblue') # create
plt.xlabel("Students") # set the x-axis label
plt.xticks(rotation=45) # rotate the x-axis labels for better visibility
plt.ylabel("Total Score") # set the y-axis label
plt.title("Student Performance") # set the title of the plot
#plt.show()

# Plotting score distribution
plt.figure(figsize=(10, 6)) # set the figure size
plt.hist(temp_students["Total"], bins=10, color='lightcoral', edgecolor='black') # create a histogram of total scores
plt.xlabel("Total Score") # set the x-axis label
plt.ylabel("Frequency") # set the y-axis label
plt.title("Score Distribution") # set the title of the plot

plt.show() 
