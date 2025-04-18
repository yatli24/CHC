# import necessary libraries
import pandas as pd
import numpy as np
import glob
import os

'''

'''

# Initialize an empty dictionary to store DataFrames
dfs_dict = {}

# initiate file list
list_of_files = glob.glob('data/csv/*')

files_path = []

for path in list_of_files:
    path_mod = path.replace('\\', '/')
    files_path.append(path_mod)

for f in files_path:
    df = pd.read_csv(f)
    if 'model' not in df.columns:
        print(f"Error: Column 'model' does not exist.")
    else:
        # Access the value in the first row (.iloc[0]) of the model column
        first_row_value = df['model'].iloc[0]

        # Compare it with the value you're looking for
        if first_row_value == 'MME':
            continue

    dfs_dict[f] = df

mme_df = pd.concat(dfs_dict.values()).groupby(['season', 'date_of_prediction', 'region', 'realization_year'])[['predicted_precip','precip']].mean().reset_index()
mme_df['model'] = 'MME'

grouped = mme_df.groupby('region')

for region, region_df in grouped:
    region_name = str(region)
    model = 'MME'
    filename = f'data/csv/{region_name}_{model}_merged_seasonal.csv'
    region_df.to_csv(filename)