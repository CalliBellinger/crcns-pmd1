
## import matlab files using scipy.io, loadmat function
MM_S1_proc = loadmat(path + "\\MM_S1_processed.mat")
# path = setting your own directory

#creates a dataframe using Data from the MM_S1_proc dictionary
MM_S1_dataframe = pd.DataFrame(MM_S1_proc['Data'][0])
#stores the names of the collumns of the dataframe to look at more easily 
MM_S1_columnnames = pd.Series(MM_S1_dataframe.columns)

## Function: data_selector() allows you to iterate through a chosen file
data_selector(column = 'neural_data_PMd', row = 78,save = False, file = MM_S1_dataframe)

## Function: data_explorer_MM_S1(), allows you to explore the data set for each file
# here is just an example of going through one file
print(str(MM_S1_columnnames))
    column = int(input('Which column do you want to access (enter #): '))
    selected_column = pd.DataFrame(MM_S1_dataframe.iloc[:,column][0])
    
    choice = input('do you want the entire dataframe [Y] or 1 row [N]: ')
    if choice == 'Y':
        print('saving yours selected dataframe as "new_dataframe"')
        new_dataframe = selected_column
    else:
        row = int(input('which of the 496 rows do you want?:  '))
        print('saving yours selected dataframe as "new_dataframe"')
        new_dataframe = selected_column.iloc[row,0]