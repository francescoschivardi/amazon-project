import json
import csv
import os
from tqdm import tqdm

def process_json(input_file, output_writer):
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

    asin = data['asin']
    seller_ids = data['data']['sellerIds']

    for date, seller_id in seller_ids.items():
        output_writer.writerow({'asin': asin, 'date': date, 'sellerId': seller_id})

if __name__ == "__main__":
    input_folder = r"data\products\time_series\top5000\MX\11782336011_productosparaanimales\BUYBOXSELLERIDHISTORY"
    output_folder = r"data\time_series_aggregate\BUY_BOX_SELLER_ID"
    output_file_name = 'buy_box_sellerId_MX.csv'

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    output_file_path = os.path.join(output_folder, output_file_name)

    with open(output_file_path, 'w', newline='') as csv_file:
        fieldnames = ['asin', 'date', 'sellerId']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for filename in tqdm(os.listdir(input_folder)):
            if filename.endswith(".json"):
                input_path = os.path.join(input_folder, filename)
                process_json(input_path, writer)


