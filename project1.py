import data_restructure as dr
import numpy as np
import math

## Calli used this to import the data, set her directory
#path = 'C:\\Users\\cebel_000\\crcns-pmd1-ceb5xe\\data_and_scripts\\source_data\\processed'

#df = dr.matlab_to_DF(path + "\\MM_S1_processed.mat")

#Variable Creation
#####################################################################################

#takes the above dataframe and seperates out the rows by individual cells
cell_seperated = dr.seperate_cells_PMd(df)

#creates variable holding the time of the reach
cell_seperated['reach_time'] = cell_seperated['reach_end'] - cell_seperated['reach_st']

#creates variable calcuating the speed of the reach
cell_seperated['reach_speed'] = cell_seperated['reach_len'] / cell_seperated['reach_time']
 
#creates a categorical variable marking slow and fast reach times
cell_seperated.insert(len(cell_seperated.columns),'reach_speed_category' , 'Medium')
cell_seperated.loc[cell_seperated['reach_speed'] >= 10, 'reach_speed_category'] = 'Slow'
cell_seperated.loc[cell_seperated['reach_speed'] <= 4, 'reach_speed_category'] = 'Fast'

#creates a variable holding the cell firings from the onset of the target (always bing #30) till 30 bins later
cell_seperated['pre_movement_spikes'] = cell_seperated.loc[:,'cell_firing_PMd'].str[29:]

#creates a variable holding the cell firing rate
cell_seperated['pre_movement_rate'] = cell_seperated['pre_movement_spikes'].apply(np.mean)

# separating reach_pos_st coordinates
cell_seperated['reach_pos_st_x'] = cell_seperated['reach_pos_st'][0]


reach_pos_StartCord = list(cell_seperated['reach_pos_st'].values)
reach_pos_EndCord = list(cell_seperated['reach_pos_end'].values)

magnitude = []
magnitude_x = []
magnitude_y = []
for i in range(len(reach_pos_StartCord)):
    reachPosSt_x = reach_pos_StartCord[i][0]
    reachPosSt_y = reach_pos_StartCord[i][1]
    
    reachPosEnd_x = reach_pos_EndCord[i][0]
    reachPosEnd_y = reach_pos_EndCord[i][1]
    
    magnitude.append(math.sqrt((reachPosEnd_x - reachPosSt_x)**2 + (reachPosEnd_y -reachPosSt_y)**2))
    magnitude_x.append(reachPosEnd_x - reachPosSt_x)
    magnitude_y.append(reachPosEnd_y - reachPosSt_y)
    
    
cell_seperated['Magnitude'] = magnitude
cell_seperated['Magnitude_x'] = magnitude_x
cell_seperated['Magnitude_y'] = magnitude_y


#creates a variable holding the angle from the starting position to the end position
cell_seperated.insert(len(cell_seperated.columns),'Theta' , 0)

def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

for a in range(len(cell_seperated)):
    start = cell_seperated.loc[a,'reach_pos_st'].astype('d')
    end = cell_seperated.loc[a,'reach_pos_end'].astype('d')
    cell_seperated.loc[i,'Theta'] = angle_between(start, end)


#creates a variable holding the angle from the starting position to the end position ( but a different way)
cell_seperated.insert(len(cell_seperated.columns),'Theta2' , 0)
for i in range(len(cell_seperated)):
    cell_seperated.loc[i,'Theta2'] = math.degrees(cell_seperated.loc[i,'reach_dir'])

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


#Exploration
#####################################################################################

#cell firing rate grouped by cell identity and Theta 
cell_firingrate_by_theta = cell_seperated.loc[:,['cell_id','Theta_category','pre_movement_rate']].groupby(['cell_id','Theta_category']).mean()







cell1= dr.select_cell(1, cell_seperated)


#
cell1['index'] = 0
cell1['reach_st'] =  cell1['reach_st'].astype('d')

for i in range(len(cell1)):
    index = np.where(cell1.loc[i,'target_on'] == 1)[0][0]
    cell1['index'][i] =  index

cell1['pre-firing'] = cell1.loc[:,'cell_firing_PMd'].str[29:44]



for i in range(len(cell1)):
    index = np.where(cell1.loc[i,'target_on'] == 1)[0][0]
    cell1['index'][i] =  index

np.where(cell1['target_on'] == 1)

np.where(cell1.loc[450,'cue_on'] == cell1.loc[450,''])


###### THE 30TH TIMESTAMP DOES ALWAYS SEEM TO CORREPSOND TO THE 'CUE ON' TIME
reach1_cue_on = cell1.loc[5,'cue_on']

reach1_timewindow = cell1.loc[5,'timestamps'][29]

len(cell1.loc[5,'timestamps']a) #116
len(cell1.loc[5,'time_window']) #420

len(cell1.loc[5,'cell_firing_PMd']) #116


#### Creates csv file to use in R studio
#exporting to R
r_dataset = cell_seperated.loc[:,['cell_id', 'Magnitude_x','Magnitude_y','Magnitude','pre_movement_rate','reach_speed','Theta','Theta_category']]

r_dataset.to_csv('Compneuro_new_new.csv')


#Plotting  ### Ended up using R to create all of our graphs
#####################################################################################

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import statsmodels.api as sm

#Histogram of Reach speed where the firing rate is not 0
num_bins = 10
speeds_not0 = np.log(cell_seperated.loc[cell_seperated['pre_movement_rate'] != 0,'reach_speed'].astype('d'))
speeds = np.log(cell_seperated['reach_speed'].astype('d'))
n , bins, patches = plt.hist(speeds_not0, num_bins, facecolor='blue', alpha=0.5)
plt.show()

#Histogram of Firing Rate where it is not 0
num_bins = 50
rates_not0 = cell_seperated.loc[cell_seperated['pre_movement_rate'] != 0,'pre_movement_rate'].astype('d')
rates = cell_seperated['pre_movement_rate'].astype('d')
n , bins, patches = plt.hist(rates_not0, num_bins, facecolor='blue', alpha=0.5)
plt.show()


#Reachspeed vs movement rate (Continuous)
plt.scatter(speeds_not0, rates_not0, alpha=0.5)
plt.title('Reachspeed vs movement rate (Continuous)')
plt.xlabel('Reach speeds')
plt.ylabel('Average firing rates')
plt.show()

#lowess regression
lowess = sm.nonparametric.lowess(speeds_not0, rates_not0)
lowess_x = list(zip(*lowess))[0]
lowess_y = list(zip(*lowess))[1]

plt.plot(lowess_x, lowess_y)
plt.scatter(rates_not0, speeds_not0, alpha=0.5, c = 'orange')
plt.title('Non-parametric Loess regression predicions of reach speed as a function of firing rate')
plt.xlabel('Average firing rates')
plt.ylabel('Reach speeds')
plt.show()


#Histogram of Reach speed where the firing rate is LOW but not == 0
num_bins = 20
reach_speeds_lowfiringrate = cell_seperated.loc[(cell_seperated['pre_movement_rate'] < .3)&(cell_seperated['pre_movement_rate'] > 0),'reach_speed'].astype('d')
plt.hist(reach_speeds_lowfiringrate, num_bins, facecolor='blue', alpha=0.5)
plt.show()

#Histogram of Reach speed where the firing rate is HIGH
num_bins = 20
reach_speeds_lowfiringrate = cell_seperated.loc[(cell_seperated['pre_movement_rate'] > .35),'reach_speed'].astype('d')
plt.hist(reach_speeds_lowfiringrate, num_bins, facecolor='blue', alpha=0.5)
plt.show()

#plots the firing rates of a cell and plots by theta category
def plot_cellfiring_by_Theta(cell = int):
    
    df = cell_seperated.loc[cell_seperated['cell_id'] == cell,['Theta_int','pre_movement_rate']].groupby(['Theta_int']).mean().reset_index() 
    df.sort_values(by = 'Theta_int', inplace = True)
    
    plt.plot(df['Theta_int'],df['pre_movement_rate'])
    plt.title(('Cell '+str(cell)+' firing rate as function of Theta'))
    plt.xlabel('Theta')
    plt.ylabel('Firing Rate')
    plt.show()


#Cells that show preference to angle = 3
plot_cellfiring_by_Theta(70)

for i in range(20):
    plot_cellfiring_by_Theta(i)    
