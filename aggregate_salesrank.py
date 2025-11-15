import json
import csv
import os
from tqdm import tqdm

folder_path = 'data/products/time_series/5000_25000/IT/12472499031_prodottiperanimalidomestici/SALESRANKS'

# Loop through each file in the folder
for filename in tqdm(os.listdir(folder_path)):
    if filename.endswith('.json'):  # Process only JSON files
        file_path = os.path.join(folder_path, filename)

        # Load JSON data from the file
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        # Specify the keys to access the desired dictionary
        key_dic1 = 'data'
        sales_rank_key = 'salesRank'

        # Check if the specified keys exist in the JSON data
        if key_dic1 in data and sales_rank_key in data[key_dic1]:
            value_dictionary = data[key_dic1][sales_rank_key]

            # Extract data for "date" and "rank" headers
            dates = list(value_dictionary.keys())  # Extract keys as dates
            ranks = list(value_dictionary.values())  # Extract values as ranks

            # Combine dates and ranks into rows
            rows = zip(dates, ranks)

            # Create a CSV file for each JSON file
            output_filename = os.path.splitext(filename)[0] + '_output.csv'
            output_file_path = os.path.join(folder_path, output_filename)

            with open(output_file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)

                # Write header
                csv_writer.writerow(['date', 'rank'])

                # Write rows
                csv_writer.writerows(rows)
        else:
            print(f"Keys not found in the JSON data for file: {filename}")











import os

folder_path = 'data/products/time_series/5000_25000/IT/12472499031_prodottiperanimalidomestici/SALESRANKS'

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):  # Check if the file has a .csv extension
        file_path = os.path.join(folder_path, filename)
        
        try:
            # Remove the CSV file
            os.remove(file_path)
            print(f"File '{filename}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting file '{filename}': {e}")

