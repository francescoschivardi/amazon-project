import json
import pandas as pd

input_file = r"data\products\time_series\top5000\DE\340852031_haustier\OFFERS\B00A0D9OGS.json"

with open(input_file, 'r') as r:
    offer_dict = json.load(r)
    data_list = offer_dict.get("data ", [])
    product_code = offer_dict.get("asin", "")  # Extracting the product code

# Create a list to store dictionaries
data_rows = []

for data in data_list:
    # Extracting values from each dictionary
    last_seen = data.get("lastSeen", "")
    seller_id = data.get("sellerId", "")
    offer_csv = data.get("offerCSV", [])
    condition = data.get("condition", "")
    is_prime = data.get("isPrime", "")
    is_map = data.get("isMAP", "")
    is_shippable = data.get("isShippable", "")
    is_addon_item = data.get("isAddonItem", "")
    is_preorder = data.get("isPreorder", "")
    is_warehouse_deal = data.get("isWarehouseDeal", "")
    is_scam = data.get("isScam", "")
    is_amazon = data.get("isAmazon", "")
    is_prime_excl = data.get("isPrimeExcl", "")
    offer_id = data.get("offerId", "")
    is_fba = data.get("isFBA", "")
    ships_from_china = data.get("shipsFromChina", "")

    # Reshape offerCSV
    offer_csv_reshaped = [(offer_csv[i], offer_csv[i + 1], offer_csv[i + 2]) for i in range(0, len(offer_csv), 3)]

    # Append data to the list
    for time, price, shipping_price in offer_csv_reshaped:
        data_rows.append({
            "product_code": product_code,
            "lastSeen": last_seen,
            "sellerId": seller_id,
            "time": time,
            "price": price,
            "shipping_price": shipping_price,
            "condition": condition,
            "isPrime": is_prime,
            "isMAP": is_map,
            "isShippable": is_shippable,
            "isAddonItem": is_addon_item,
            "isPreorder": is_preorder,
            "isWarehouseDeal": is_warehouse_deal,
            "isScam": is_scam,
            "isAmazon": is_amazon,
            "isPrimeExcl": is_prime_excl,
            "offerId": offer_id,
            "isFBA": is_fba,
            "shipsFromChina": ships_from_china
        })

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data_rows)

# Write the DataFrame to a CSV file
csv_filename = "output.csv"
df.to_csv(csv_filename, index=False)

print(f"CSV file '{csv_filename}' created successfully.")













import os
import json
import pandas as pd
import keepa_new
from tqdm import tqdm


# Specify the directory containing your JSON files
json_directory = r"C:\Users\franc\Documents\amazon\data\products\time_series\top5000\MX\11782336011_productosparaanimales\OFFERS"

# Initialize an empty list to store DataFrames
all_data_frames = []

# Iterate through all JSON files in the directory
for filename in tqdm(os.listdir(json_directory)):
    try:
    
        if filename.endswith(".json"):
            file_path = os.path.join(json_directory, filename)

            with open(file_path, 'r') as file:
                offer_dict = json.load(file)
                data_list = offer_dict.get("data ", [])
                product_code = offer_dict.get("asin", "")

            # Create a list to store dictionaries
            data_rows = []

            for data in data_list:
                # Extracting values from each dictionary
                last_seen = data.get("lastSeen", "")
                seller_id = data.get("sellerId", "")
                offer_csv = data.get("offerCSV", [])
                condition = data.get("condition", "")
                is_prime = data.get("isPrime", "")
                is_map = data.get("isMAP", "")
                is_shippable = data.get("isShippable", "")
                is_addon_item = data.get("isAddonItem", "")
                is_preorder = data.get("isPreorder", "")
                is_warehouse_deal = data.get("isWarehouseDeal", "")
                is_scam = data.get("isScam", "")
                is_amazon = data.get("isAmazon", "")
                is_prime_excl = data.get("isPrimeExcl", "")
                offer_id = data.get("offerId", "")
                is_fba = data.get("isFBA", "")
                ships_from_china = data.get("shipsFromChina", "")

                # Reshape offerCSV
                offer_csv_reshaped = [(offer_csv[i], offer_csv[i + 1], offer_csv[i + 2]) for i in range(0, len(offer_csv), 3)]

                # Append data to the list
                for time, price, shipping_price in offer_csv_reshaped:
                    data_rows.append({
                        "product_code": product_code,
                        "lastSeen": last_seen,
                        "sellerId": seller_id,
                        "time": time,
                        "price": price,
                        "shipping_price": shipping_price,
                        "condition": condition,
                        "isPrime": is_prime,
                        "isMAP": is_map,
                        "isShippable": is_shippable,
                        "isAddonItem": is_addon_item,
                        "isPreorder": is_preorder,
                        "isWarehouseDeal": is_warehouse_deal,
                        "isScam": is_scam,
                        "isAmazon": is_amazon,
                        "isPrimeExcl": is_prime_excl,
                        "offerId": offer_id,
                        "isFBA": is_fba,
                        "shipsFromChina": ships_from_china
                    })

            # Create a DataFrame from the list of dictionaries
            df = pd.DataFrame(data_rows)

            # Append the DataFrame to the list
            all_data_frames.append(df)
    except TypeError:
        continue

# Concatenate all DataFrames into one aggregated DataFrame
aggregated_df = pd.concat(all_data_frames, ignore_index=True)
time_col = ["time"]
aggregated_df[time_col] = aggregated_df[time_col].apply(keepa_new.keepa_minutes_to_time).apply(pd.to_datetime).apply(lambda x: x.dt.strftime('%Y-%m-%d'))

# Write the aggregated DataFrame to a CSV file
output_path = "data/time_series_aggregate/OFFER"
csv_filename = "MX_offer_aggregated.csv"
aggregated_df.to_csv(os.path.join(output_path, csv_filename), index=False)

print(f"Aggregated CSV file '{csv_filename}' created successfully.")

