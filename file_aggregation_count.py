import os
import pandas as pd
from tqdm import tqdm

# Specify the folder where your original CSV files are located
input_folder_path = r"data\products\time_series\top5000\MX\11782336011_productosparaanimales\COUNT_NEW"

# Specify the folder where you want to save the modified CSV files
output_folder_path = input_folder_path + '/COUNT_NEW_MODIFIED'

#output_folder_path = 'data/products/time_series/top5000/DE/340852031_haustier/COUNT_NEW/COUNT_NEW_MODIFIED'

# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Get a list of all CSV files in the input folder
csv_files = [file for file in os.listdir(input_folder_path) if file.endswith('.csv')]

# Loop through each CSV file
for csv_file in tqdm(csv_files):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(os.path.join(input_folder_path, csv_file))
        
    # Set the column names to "date" and "count"
    df.columns = ["date", "count"]
        
    # Extract the product code (file name without ".csv" extension)
    product_code = os.path.splitext(csv_file)[0]
        
    # Add the "product_code" column with the modified file name
    df["product_code"] = product_code
        
    # Save the modified DataFrame to the output folder with a new file name
    output_file_path = os.path.join(output_folder_path, f"{product_code}_modified.csv")
    df.to_csv(output_file_path, index=False)

print("CSV files have been modified and saved to the specified output folder.")


import os
import pandas as pd
from tqdm import tqdm


# Get a list of all modified CSV files in the folder
csv_files = [file for file in os.listdir(output_folder_path) if file.endswith('.csv')]

# Loop through each modified CSV file
for csv_file in tqdm(csv_files):
    # Read the modified CSV file into a pandas DataFrame
    df = pd.read_csv(os.path.join(output_folder_path, csv_file))
    
    # Delete rows where the "count" column is blank
    df = df.dropna(subset=["count"])
    
    # Now you have a DataFrame with rows removed, and you can continue to work with it

# If you want to save the modified DataFrames back to the CSV files, you can add the following code after the loop:
    df.to_csv(os.path.join(output_folder_path, csv_file), index=False)



import os
import pandas as pd
from tqdm import tqdm


output_path = "data/time_series_aggregate/COUNT_NEW/top5000"

# Get a list of all modified CSV files in the folder
csv_files = [file for file in os.listdir(output_folder_path) if file.endswith('.csv')]

# Initialize an empty list to store the DataFrames
dfs = []

# Loop through each modified CSV file
for csv_file in tqdm(csv_files):
    # Read the modified CSV file into a pandas DataFrame
    df = pd.read_csv(os.path.join(output_folder_path, csv_file))
    
    # Append the DataFrame to the list
    dfs.append(df)

# Concatenate the DataFrames vertically while preserving column headers
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv(os.path.join(output_path, 'MX_merged_file.csv'), index=False)

print("CSV files have been merged vertically into 'merged_file.csv'.")