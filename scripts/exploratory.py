#Nadav Ivzan exploratory code

#imports
import matplotlib.pyplot as plt 
import pandas as pd
import math as m
from sklearn import datasets

def int_plus_1(int_var: int)->int:
    '''
    this function takes an input and returns + 1
    parameters: int_var
    returns: int_return

    ''' 
    int_return=int_var+1
    return int_return

def int_times_two(int_var: int) -> int:
    """
    This function takes an integer as input and returns that integer times 2

    Parameters: int_var
    Returns: int_var_times_two
    """

    return int_var*2

if __name__ == '__main__':
    print("Hello! This is exploratory code")
    var_1 = 10
    print(int_plus_1(var_1))
    var_2 = 20
    print(int_times_two(var_2))

    #Load iris data set into main program
    iris=datasets.load_iris()

    #homework shift iris to panda dataset
    #install plotly in virtual environment
    # update requirements txt
    # push all the changes to main branch in github 