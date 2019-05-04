#Exploratory scratch code
#####################################################################################

#cell firing rate grouped by cell identity and Theta 
cell_firingrate_by_theta = cell_seperated.loc[:,['cell_id','Theta_category','pre_movement_rate']].groupby(['cell_id','Theta_category']).mean()

#Plotting
#####################################################################################

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import statsmodels.api as sm

#Histogram of Reach speed where the firing rate is not 0
num_bins = 10
speeds_not0 = cell_seperated.loc[cell_seperated['pre_movement_rate'] != 0,'reach_speed'].astype('d')
speeds = cell_seperated['reach_speed'].astype('d')
n , bins, patches = plt.hist(speeds, num_bins, facecolor='blue', edgecolor = 'black', alpha=0.5)
plt.title('Reach Speed')
plt.xlabel('Reach Speed (cm/s)')
plt.ylabel('Count')
plt.show()

#Histogram of Firing Rate where it is not 0
num_bins = 20
rates_not0 = cell_seperated.loc[cell_seperated['pre_movement_rate'] != 0,'pre_movement_rate'].astype('d')
rates = cell_seperated['pre_movement_rate'].astype('d')
n , bins, patches = plt.hist(rates, num_bins, facecolor='blue', edgecolor = 'black', alpha=0.5)
plt.title('Histogram of Firing Rate')
plt.xlabel('Firing Rate (Spikes per Second)')
plt.ylabel('Count')
plt.show()


#Reachspeed vs movement rate (Continuous)
plt.scatter(speeds_not0, rates_not0, alpha=0.5)
plt.title('Reach Speed Vs Firing Rate')
plt.ylabel('Reach Speed (cm/s)')
plt.xlabel('Firing Rate (Spikes per Second)')
plt.show()

#lowess regression
lowess = sm.nonparametric.lowess(speeds_not0, rates_not0)
lowess_x = list(zip(*lowess))[0]
lowess_y = list(zip(*lowess))[1]

plt.plot(lowess_x, lowess_y)
plt.scatter(rates_not0, speeds_not0, alpha=0.5, c = 'orange')
plt.title('Loess Regression for Reach Speed as Function of Firing Rate')
plt.ylabel('Reach Speed (cm/s)')
plt.xlabel('Firing Rate (Spikes per Second)')
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
    plt.title(('Cell '+str(cell)+' Firing Rate as Function of Theta'))
    plt.xlabel('Theta (degrees)')
    plt.ylabel('Firing Rate')
    plt.show()

#Cells that show preference to angle = 3
for i in range(73,78):
    plot_cellfiring_by_Theta(i)