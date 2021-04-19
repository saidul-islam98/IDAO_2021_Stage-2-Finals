import pathlib as path

import numpy as np
import pandas as pd

from utils import make_map, mappify, sort_and_map

def process_product_code(df, client_ids):

    mp = {
        'Current accounts': 0,
        'Time account': 1,
        'Broker': 2,
        'UK': 3,
        'NSJ': 4,
        'ILI': 5
    }
    r = []
    for id in client_ids:
        rows = df[df['client_id']==id]
        codes = [0]*len(mp)
        if not rows.empty:
            unq = rows['product_code'].unique()
            for x in unq:
                codes[mp[x]] = 1
        r.append(codes)
    r = np.array(r)
    print('product_code',r.shape)
    return r

def load_x(df, client_ids):

    #one-to-many
    product_code = process_product_code(df, client_ids)

    return product_code