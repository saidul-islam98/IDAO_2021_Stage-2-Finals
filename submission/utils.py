from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pathlib as path

import numpy as np
import pandas as pd

def one_hot_encoder(values):
    
    values = values.to_numpy().astype(str)
    debug = False
    
    if debug: print(values)
    # integer encode
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values)
    if debug: print(integer_encoded)
    # binary encode
    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    if debug: print(onehot_encoded)
    return onehot_encoded

def make_map(col):

    values = col.unique()
    mp = {}
    for i, value in enumerate(values):
        mp[value] = i
    #print(mp)
    return mp

def mappify(df):
    df.replace(np.nan, 'nan')
    return df.map(make_map(df)).to_numpy()

def sort_and_map(df, name, client_ids):
    values = []
    for id in client_ids:
        row = df[df['client_id']==id]
        if row.empty:
            values.append(np.nan)
        else:
            values.append(row[name])
    df = pd.DataFrame()
    df[name] = values
    print(len(df))
    print(df)
    return mappify(df)

def split(x):
    
    ind = int(len(x)*.75)

    train = x[:ind]
    val = x[ind:]
    
    return train, val