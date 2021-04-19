import pathlib as path

import numpy as np
import pandas as pd

from utils import make_map, mappify, sort_and_map

import process_aum, process_trxn

def load_x(client, aum, trxn):
    
    #client_ids
    client_ids = client['client_id'].to_numpy()
    #client
    gender = mappify(client['gender'])
    print('gender',gender.shape)
    age = client['age'].to_numpy()
    print('age',age.shape)
    region = client['region'].to_numpy()
    print('region',region.shape)
    city = client['city'].to_numpy()
    print('city',city.shape)
    education = mappify(client['education'])
    print('education',education.shape)
    job_type = mappify(client['job_type'])
    print('job_type',job_type.shape)
    #aum
    aum_data = process_aum.load_x(aum, client_ids)
    print('aum_data',aum_data.shape)
    #trxn
    trxn_data = process_trxn.load_x(trxn, client_ids)
    print('trxn_data',trxn_data.shape)

    #make x
    x = np.column_stack((gender,age,region,city,education,job_type,aum_data,trxn_data))

    print('x',x.shape)

    return x, client_ids

def load_y(df, client_ids):

    y = []
    for id in client_ids:
        row = df[df['client_id']==id]
        y.append(row['sale_flg'])
    y = np.array(y)
    return y.flatten()

def load_data(mode, cfg):

    DATA_FOLDER = path.Path(cfg["DATA"]["DatasetPath"])

    client = pd.read_csv(f'{DATA_FOLDER}/{cfg["DATA"]["client"]}')
    aum = pd.read_csv(f'{DATA_FOLDER}/{cfg["DATA"]["aum"]}')
    trxn = pd.read_csv(f'{DATA_FOLDER}/{cfg["DATA"]["trxn"]}')

    if mode=='train':
        funnel = pd.read_csv(f'{DATA_FOLDER}/{cfg["DATA"]["funnel"]}')

    #make x and y
    x, client_ids = load_x(client, aum, trxn)
    if mode=='train':
        y = load_y(funnel, client_ids)

    if mode=='train':
        return x, y
    else:
        return x, client_ids