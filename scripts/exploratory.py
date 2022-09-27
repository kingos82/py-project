#Nadav Ivzan exploratory code

#imports
import matplotlib.pyplot as plt 
import pandas as pd
import math as m

def int_plus_1(int_var: int)->int:
    '''
    this function takes an input and returns + 1
    parameters: int_var
    returns: int_return

    ''' 
    int_return=int_var+1
    return int_return

if __name__ == '__main__':
    print(int_plus_1(10))