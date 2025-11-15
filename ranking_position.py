import csv
import json


# Replace 'your_input.json' with your actual input JSON file path
json_input_path = r'data\top5000\US_2619533011_petsupplies_top5000.json'

# Replace 'your_output.csv' with your desired output CSV file path
csv_output_path = r'C:\Users\franc\Documents\amazon\data\products_ranked\US_top5000.csv'

# Load the JSON file
with open(json_input_path) as json_file:
    data = json.load(json_file)

# Extract values from the list under "asins"
product_list = data.get("asins", [])

# Write to CSV
with open(csv_output_path, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(["product_code"])
    
    # Write each product code from the list
    for product_code in product_list:
        writer.writerow([product_code])

print(f"CSV file '{csv_output_path}' created successfully.")
