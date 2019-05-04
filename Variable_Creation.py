import data_restructure as dr
import numpy as np
import math

df = dr.matlab_to_DF("MM_S1_processed.mat")

#Variable Creation
#####################################################################################

#takes the above dataframe and seperates out the rows by individual cells
cell_seperated = dr.seperate_cells_PMd(df)

#creates variable holding the time of the reach
cell_seperated['reach_time'] = cell_seperated['reach_end'] - cell_seperated['reach_st']

#creates variable calcuating the speed of the reach
cell_seperated['reach_speed'] = cell_seperated['reach_len'] / cell_seperated['reach_time']
 
#creates a categorical variable marking slow and fast reach times, with default value == Medium
cell_seperated.insert(len(cell_seperated.columns),'reach_speed_category' , 'Medium')
cell_seperated.loc[cell_seperated['reach_speed'] <= 4, 'reach_speed_category'] = 'Slow'
cell_seperated.loc[cell_seperated['reach_speed'] >= 10, 'reach_speed_category'] = 'Fast'

#creates a variable holding the cell firings from the onset of the target (always bing #30) till 30 bins later
cell_seperated['pre_movement_spikes'] = cell_seperated.loc[:,'cell_firing_PMd'].str[29:59]

#creates a variable holding the cell firing rate and converts it to 'per second' from 'per 10 Ms'
cell_seperated['pre_movement_rate'] = cell_seperated['pre_movement_spikes'].apply(np.mean) * 100

#creates a variable holding the angle from the starting position to the end position, (default value == 0)
cell_seperated.insert(len(cell_seperated.columns),'Theta' ,0)

def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

for i in range(len(cell_seperated)):
    start = cell_seperated.loc[i,'reach_pos_st'].astype('d')
    end = cell_seperated.loc[i,'reach_pos_end'].astype('d')
    cell_seperated.loc[i,'Theta'] = angle_between(start, end)


#creates a variable holding the angle from the starting position to the end position ( but a different way using variable reach_dir)
cell_seperated.insert(len(cell_seperated.columns),'Theta_radians' , 0)
for i in range(len(cell_seperated)):
    cell_seperated.loc[i,'Theta_radians'] = math.degrees(cell_seperated.loc[i,'reach_dir'])

#creates a categorical variable for 'Theta' in 20 degree increments
cell_seperated.insert(len(cell_seperated.columns),'Theta_category' , 0)
for i in range(len(cell_seperated)):
    if (cell_seperated.loc[i,'Theta'] >= 0) & (cell_seperated.loc[i,'Theta'] < 20):
        cell_seperated.loc[i,'Theta_category'] = '0-20'
    elif (cell_seperated.loc[i,'Theta'] >= 20) & (cell_seperated.loc[i,'Theta'] < 40):
        cell_seperated.loc[i,'Theta_category'] = '20-40'    
    elif (cell_seperated.loc[i,'Theta'] >= 40) & (cell_seperated.loc[i,'Theta'] < 60):
        cell_seperated.loc[i,'Theta_category'] = '40-60'    
    elif (cell_seperated.loc[i,'Theta'] >= 60) & (cell_seperated.loc[i,'Theta'] < 80):
        cell_seperated.loc[i,'Theta_category'] = '60-80'
    elif (cell_seperated.loc[i,'Theta'] >= 80) & (cell_seperated.loc[i,'Theta'] < 100):
        cell_seperated.loc[i,'Theta_category'] = '80-100'
    elif (cell_seperated.loc[i,'Theta'] >= 100) & (cell_seperated.loc[i,'Theta'] < 120):
        cell_seperated.loc[i,'Theta_category'] = '100-120'
    elif (cell_seperated.loc[i,'Theta'] >= 120) & (cell_seperated.loc[i,'Theta'] < 140):
        cell_seperated.loc[i,'Theta_category'] = '120-140'
    elif (cell_seperated.loc[i,'Theta'] >= 140) & (cell_seperated.loc[i,'Theta'] < 160):
        cell_seperated.loc[i,'Theta_category'] = '140-160'
    elif (cell_seperated.loc[i,'Theta'] >= 160) & (cell_seperated.loc[i,'Theta'] < 180):
        cell_seperated.loc[i,'Theta_category'] = '160-180'
        
    elif (cell_seperated.loc[i,'Theta'] >= 180) & (cell_seperated.loc[i,'Theta'] < 200):
        cell_seperated.loc[i,'Theta_category'] = '180-200'
    elif (cell_seperated.loc[i,'Theta'] >= 200) & (cell_seperated.loc[i,'Theta'] < 220):
        cell_seperated.loc[i,'Theta_category'] = '200-220'    
    elif (cell_seperated.loc[i,'Theta'] >= 220) & (cell_seperated.loc[i,'Theta'] < 240):
        cell_seperated.loc[i,'Theta_category'] = '220-240'    
    elif (cell_seperated.loc[i,'Theta'] >= 240) & (cell_seperated.loc[i,'Theta'] < 260):
        cell_seperated.loc[i,'Theta_category'] = '240-260'
    elif (cell_seperated.loc[i,'Theta'] >= 260) & (cell_seperated.loc[i,'Theta'] < 280):
        cell_seperated.loc[i,'Theta_category'] = '260-280'
    elif (cell_seperated.loc[i,'Theta'] >= 280) & (cell_seperated.loc[i,'Theta'] < 300):
        cell_seperated.loc[i,'Theta_category'] = '280-300'
    elif (cell_seperated.loc[i,'Theta'] >= 300) & (cell_seperated.loc[i,'Theta'] < 320):
        cell_seperated.loc[i,'Theta_category'] = '300-320'
    elif (cell_seperated.loc[i,'Theta'] >= 320) & (cell_seperated.loc[i,'Theta'] < 340):
        cell_seperated.loc[i,'Theta_category'] = '320-340'
    elif (cell_seperated.loc[i,'Theta'] >= 340) & (cell_seperated.loc[i,'Theta'] < 360):
        cell_seperated.loc[i,'Theta_category'] = '340-360'       

#creating an int variable of the above theta categories for easier graphing
cell_seperated['Theta_int'] = cell_seperated['Theta_category'].str.split('-').str[0].astype('d')

#creating variables for x and y magnitude of the reach
reach_pos_StartCord = list(cell_seperated['reach_pos_st'].values)
reach_pos_EndCord = list(cell_seperated['reach_pos_end'].values)

magnitude_x = []
magnitude_y = []

for i in range(len(reach_pos_StartCord)):
    reachPosSt_x = reach_pos_StartCord[i][0]
    reachPosSt_y = reach_pos_StartCord[i][1]
    
    reachPosEnd_x = reach_pos_EndCord[i][0]
    reachPosEnd_y = reach_pos_EndCord[i][1]
    magnitude_x.append(reachPosEnd_x - reachPosSt_x)
    magnitude_y.append(reachPosEnd_y - reachPosSt_y)
    
cell_seperated['Reach_x'] = magnitude_x
cell_seperated['Reach_y'] = magnitude_y

#fixing NA value in cell_ID
for i in range(len(cell_seperated['cell_id'])):
    #making the nan values into cell #94
    if cell_seperated.loc[i,['cell_id']].astype(str)[0] == 'nan':
        cell_seperated.loc[i,['cell_id']] = 94
    #casting the cell_ID's back into integers like they should be
    cell_seperated.loc[i,['cell_id']] = cell_seperated.loc[i,['cell_id']].astype(int)
    
    
cell_seperated['cell_id'].groupby(cell_seperated['cell_id']).count()

