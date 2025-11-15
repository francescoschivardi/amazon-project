


import os
import csv
import pandas as pd
from tqdm import tqdm

# Function to remove the first row from a CSV file
def remove_first_row_from_csv(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    # Check if the file is not empty and has more than one row
    if len(rows) > 1:
        rows.pop(0)  # Remove the first row
    
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)
        print(f"Removed the first row from {file_path}")
    else:
        print(f"{file_path} is empty or has only one row. Skipping...")

# Folder path where CSV files are located
folder_path = 'data/products/time_series/5001_25000/GB/340840031_petsupplies/BUY_BOX_SHIPPING'

# List all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is a CSV file
    if filename.endswith('.csv'):
        remove_first_row_from_csv(file_path)

# List all CSV files in the folder (uncomment this line and specify the folder path)
folder_path = 'data/products/time_series/5001_25000/GB/340840031_petsupplies/BUY_BOX_SHIPPING'
csv_files = [filename for filename in os.listdir(folder_path) if filename.endswith('.csv')]
output_path1 = 'data/time_series_aggregate'

# Check if there are CSV files in the folder
if not csv_files:
    print("No CSV files found in the folder.")
else:
    combined_df = None  # Initialize an empty DataFrame

    # Loop through the CSV files and concatenate columns horizontally
    for csv_file in tqdm(csv_files):
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)
        
        # Create a new DataFrame with just one row for the filename
        file_name_without_extension = os.path.splitext(csv_file)[0]
        filename_df = pd.DataFrame([[file_name_without_extension] * len(df.columns)], columns=df.columns)
        
        # Concatenate the new header row with the data
        df = pd.concat([filename_df, df], ignore_index=True)
        
        if combined_df is None:
            combined_df = df
        else:
            combined_df = pd.concat([combined_df, df], axis=1)

    # Remove columns starting with "concatenated"
    combined_df = combined_df.loc[:, ~combined_df.columns.str.startswith('concatenated')]

    # Create a new CSV file with concatenated data
    output_file = 'GB_5001_25000_concatenated_output.csv'
    output_path = os.path.join(output_path1, output_file)
    combined_df.to_csv(output_path, index=False)
    
    print(f"Concatenated data saved to {output_path}")











import pandas as pd
import os
# Specify the path to your CSV file
csv_file_path = 'data/products/time_series/top5000/DE/340852031_haustier/COUNT_NEW'

# Read the first row of the CSV file
with open(csv_file_path, 'r') as file:
    first_row = file.readline()

# Split the first row into columns using a common delimiter (e.g., a comma)
columns = first_row.strip().split(',')

# Print the number of columns
print(f"Number of columns in the CSV file: {len(columns)}")


