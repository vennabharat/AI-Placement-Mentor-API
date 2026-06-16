import numpy as np

def evaluate(aptitude: int, communication: int, coding: int):   # Function for calculation total & average
    total = aptitude + communication + coding
    average = total/3
    return np.array([total, average])
