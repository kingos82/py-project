#Nadav Ivzan exploratory code

#imports 
import pandas as pd
from sklearn import datasets
import plotly as px 
#typecasting
def cscat(df0: pd.DataFrame, p1: str, p2: str): 
    """
    choose scatter
    this function generates a scatter plot of variables p1 & p2
    df0 dataframe
    p1 is the first parameter 
    p2 second parameter
    
    output scatter plot
    """
    try:
        fig=px.plot(data_frame=df0,
            x=p1,
            y=p2,
            kind='scatter',
            title=p1+' vs '+p2, #f"{p1} vs {p2}"
            color="class")
        return fig
    except KeyError: 
        print('error in cscat')



def cbox(df0: pd.DataFrame, p1: str): 
    """
    choose box
    this function generates a box plot of variable p1 
    df0 dataframe
    p1 is the first parameter 
    
    output box plot
    """
    try:
        fig=px.plot(data_frame=df0,
            x="class",
            y=p1,
            kind='box',
            title=p1)
            #color="class")
        return fig
    except KeyError:
        print(f"{p1} not found in dataframe")

def strt():
    '''
    This function reads and cleans the iris dataset to a dataframe object 
    '''
    #Load iris data set into main program
    iris=datasets.load_iris()
    #print(iris.keys)

    #homework shift iris to panda dataset
    df0=pd.DataFrame(iris.data, columns=iris.feature_names)
    df0['class']=iris.target

    map_dic={0:"setosa", 1:"versicolor", 2:"virginica"}

    df0['class']=df0['class'].map(map_dic)
    return df0, iris


def main():

    df0, iris =strt()
    p=iris.feature_names
    p0=''
    for x in p:
        p0+=x+', '
    try:
        p1=input('Enter 1 of 4 parameters: '+p0)
        
        p.remove(p1)

        p0=''
        for x in p:
            p0+=x+', '
        p2=input('Enter 1 of 3 parameters: '+p0)

        #generating scatter plot and box plots for p1 and p2
        f0=cscat(df0, p1, p2)
        f0.show()
        f1=cbox(df0, p1)
        f1.show()
        f2=cbox(df0, p2)
        f2.show()

    except ValueError:
        print(f"received {p1} as input but this value is not in data frame")  


    
if __name__ == '__main__':
    main()