#Nadav Ivzan exploratory code

#imports 
import pandas as pd
from sklearn import datasets
import plotly as px 

def cscat(p1: str, p2: str): 
    """
    choose scatter
    this function generates a scatter plot of variables p1 & p2

    p1 is the first parameter 
    p2 second parameter
    
    output scatter plot
    """

    fig=px.plot(data_frame=df0,
        x=p1,
        y=p2,
        kind='scatter',
        title=p1+' vs '+p2, #f"{p1} vs {p2}"
        color="class")
    return fig

if __name__ == '__main__':
 
    #Load iris data set into main program
    iris=datasets.load_iris()
    print(iris.keys)

    #homework shift iris to panda dataset
    df0=pd.DataFrame(iris.data, columns=iris.feature_names)
    df0['class']=iris.target

    map_dic={0:"setosa", 1:"versicolor", 2:"virginica"}

    df0['class']=df0['class'].map(map_dic)

    
