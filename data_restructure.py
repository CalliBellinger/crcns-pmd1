import scipy as scp
import numpy as np
from scipy.io import loadmat
import pandas as pd
import matplotlib.pyplot as plt


###function####
def matlab_to_DF(file = str):
    from scipy.io import loadmat
    import pandas as pd
    mat_data = loadmat(file)['Data'][0][0]
    
    newdf = pd.DataFrame(columns = pd.DataFrame(loadmat(file)['Data'][0]).columns, index = range(len(mat_data[0])))

    for row in range(len(mat_data[0])):
        from itertools import chain
    
        int_columns = chain(range(2)) #0,1
        float_columns = chain(range(2,5), range(7,9)) #2,3,4,7,8
        array_columns = chain(range(9,13),range(14,16))
        
        #0 = 'trial_num' = int
        #1 = 'reach_num = int
        for column in int_columns:
            newdf.iloc[row,column] = int(mat_data[column][row])
            
        #2 = 'reach_st' = float
        #3 = 'cue_on' = float
        #4 =  'reach_end' = float
        #7 = 'reach_dir' = float
        #8 = 'reach_len' = float
        for column in float_columns:
            newdf.iloc[row,column]= float(mat_data[column][row]) #[0][0].astype('d')
                
        #positional variables: Structure = [xpos,ypos]    
        #5 = starting reach position
        #6 = ending reach position
        for column in range(5,7):
            newdf.iloc[row,column] = mat_data[column][row][0][0]
            
        #9 = 'target_on' =  1 column , X# rows [reach0 = 97rows]
        #10 = 'kinematics'= 6 columns, X# rows [reach0 = 97rows]
        #11 = 'neural_data_PMd' = X#columns, 94 rows [reach0 = 97 columns]
        #12 = 'neural_data_M1' = X#columns, 67 rows [reach0 = 97 columns
        #14 = 'time_window' = 1 column, X(+)# rows   [reach0 = 418rows]
        #15 = 'timestamps' =  1 column, X# rows [reach0 = 97rows ]    
        for column in array_columns:
            newdf.iloc[row,column] = mat_data[column][row][0]
    
        #13 = 'Block Info' = I do not know whats going on with this variable    
        #for column in range (13,14):
        #    new.iloc[row,column] = mat_data[column][row]

    return newdf


def seperate_cells_PMd(df = pd.DataFrame() ):
    df_by_cell = pd.DataFrame()
    for i in range(len(df['neural_data_PMd'][0])):
        df_cell = df
        df_cell['cell_firing_PMd'] = df['neural_data_PMd'].str[i]        
        df_by_cell = df_by_cell.append(df_cell, ignore_index = True)
        df_cell['cell_id'] = i + 1
        
    df_by_cell.drop(columns = ['neural_data_PMd', 'neural_data_M1'], inplace = True)    
    return df_by_cell    


def select_cell(cellnum, df= pd.DataFrame()):
    return df.loc[df['cell_id'] == cellnum,:]


