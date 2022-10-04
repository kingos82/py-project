import pandas as pd
import pytest
#import scripts.exploratory as ex
import scripts 

#__init_.py makes the modules visible across different levels of the folder structure 

def check_column_type():
    df, iris =scripts.exploratory.strt()
    assert type(df)==pd.DataFrame
