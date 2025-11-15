import os
import pandas as pd
from tqdm import tqdm


# Specify the folder where your CSV files are located
folder_path = r'data\products\time_series\top5000\MX\11782336011_productosparaanimales\NEW_FBM_SHIPPING'

# Get a list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Loop through each CSV file
for csv_file in tqdm(csv_files):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(os.path.join(folder_path, csv_file))
        
    # Set the column names to "date" and "price"
    df.columns = ["date", "price"]
        
    # Extract the product code (file name without ".csv" extension)
    product_code = os.path.splitext(csv_file)[0]
        
    # Add the "product_code" column with the modified file name
    df["product_code"] = product_code
        
    # Save the modified DataFrame back to the same CSV file
    df.to_csv(os.path.join(folder_path, csv_file), index=False)
    

print("CSV files have been modified as per your requirements.")


import os
import pandas as pd
from tqdm import tqdm


# Get a list of all modified CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Loop through each modified CSV file
for csv_file in tqdm(csv_files):
    # Read the modified CSV file into a pandas DataFrame
    df = pd.read_csv(os.path.join(folder_path, csv_file))
    
    # Delete rows where the "price" column is blank
    df = df.dropna(subset=["price"])
    
    # Now you have a DataFrame with rows removed, and you can continue to work with it

# If you want to save the modified DataFrames back to the CSV files, you can add the following code after the loop:
    df.to_csv(os.path.join(folder_path, csv_file), index=False)



import os
import pandas as pd
from tqdm import tqdm


output_path = r'data\time_series_aggregate\NEW_FBM_SHIPPING\top5000'

# Get a list of all modified CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Initialize an empty list to store the DataFrames
dfs = []

# Loop through each modified CSV file
for csv_file in tqdm(csv_files):
    # Read the modified CSV file into a pandas DataFrame
    df = pd.read_csv(os.path.join(folder_path, csv_file))
    
    # Append the DataFrame to the list
    dfs.append(df)

# Concatenate the DataFrames vertically while preserving column headers
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv(os.path.join(output_path, 'MX_merged_file.csv'), index=False)

print("CSV files have been merged vertically into 'merged_file.csv'.")