import os
import json
import pandas as pd
from tqdm import tqdm
import keepa_new

input_path = r'data\products\static\top5000\MX\11782336011_productosparaanimales'

product_dfs = []

for json_file in tqdm(os.listdir(input_path)):
    r = open(os.path.join(input_path, json_file))
    product_dict = json.load(r) 
    product_df = pd.DataFrame.from_dict(product_dict, orient='index')
    product_dfs.append(product_df.T)

out = pd.concat(product_dfs)
out.reset_index(drop = True, inplace=True)

# clean time columns
time_cols = ['lastUpdate', 'lastPriceChange',
             'trackingSince', 'publicationDate',
            'releaseDate', 'lastRatingUpdate', 'listedSince']
out[time_cols] = out[time_cols].apply(keepa_new.keepa_minutes_to_time).apply(pd.to_datetime).apply(lambda x: x.dt.strftime('%Y-%m-%d'))


out.to_csv(os.path.join('data/static_aggregate/','MX_top5000.csv'), index=False)

out['lastUpdate'].dt.strftime("%Y, %m, %d")
