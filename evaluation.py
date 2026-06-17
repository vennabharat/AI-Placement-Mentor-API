import numpy as np  # importing numarical python for array operations

# Function for calculating total & average from student scores
def evaluate(aptitude: int, communication: int, coding: int):   
    total = aptitude + communication + coding
    average = total/3
    return np.array([total, average])
