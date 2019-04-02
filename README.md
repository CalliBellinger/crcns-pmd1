
# Computational Neuroscience Project Skeleton

This repository is a skeleton Python package that students in PSYC 5270 can use to get started on their data exploration assignments.

## Getting started

Start by cloning the repository: `git clone https://github.com/melizalab/comp-neurosci-skeleton.git`

This will create a new directory, `comp-neurosci-skeleton`, containing the following items:

- `README.md`: this file
- `setup.py`:  package description file. You will need to edit this.
- `requirements.txt`: a list of packages your code depends on
- `.gitignore`: a list of files git will ignore when telling you what's changed
- `src`:       a directory where you will put your python code
- `test`:      a directory where you will put test code
- `data`:      a directory where your data will live
- `build`:     a directory where processed output from your analysis will live

Choose a new name for your package. Rename the top-level directory (`comp-neurosci-skeleton`) and edit `setup.py` to set the new name and other identifying information.

Now you need to create a github repository of your own. Go to [https://github.com/new](https://github.com/new). Give the repository your chosen name and a description, then click Create Repository. Make a note of the address of your repository. It will look something like `https://github.com/dmeliza/dummy.git`

Finally, set your local directory to track the github repository by running the following commands in your working directory. Replace the repository address in the code below with the one for your project.

``` shell
git remote rm origin
git remote add origin https://github.com/dmeliza/dummy.git
git push -u origin master
```

## Next steps

Edit `data/README.md` to describe how to retrieve data. Better yet, write a script.

Edit `requirements.txt` to add any needed dependencies, then create a virtual environment and install the dependencies as follows:

``` shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Install the project in development mode by running `python setup.py develop`. If you use notebooks, this will ensure that you can access your modules.

Edit this file to describe your actual project.

## How to access files:
- load matlab files using scipy.io, loadmat function
- use function "data_selector" to iterate through the file

```shell
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
```
### Files used:
- crcns-pmd1-ceb5xe\data_and_scripts\source_data\processed
- Files used as of now (4/2):
    - MM_S1_processed.mat
    - MT_S1_processed.mat
    - MT_S2_proccessed.mat
    - MT_S3_processed.mat
- We can either compare monkey MM to monket MT OR
- Look at monkey MT's learning/memory as MT goes through 3 sessions
