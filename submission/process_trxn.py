import pathlib as path

import numpy as np
import pandas as pd

from utils import make_map, mappify, sort_and_map

def process_card_count(df, client_ids):

    r=[]
    for id in client_ids:
        card_count = 0
        rows = df[df['client_id']==id]
        if not rows.empty:
            cards = rows['card_id'].unique()
            card_count = len(cards)
        r.append(card_count)
    r = np.array(r)
    print('card_count',r.shape)
    return r

def process_avg_trxn_amount(df, client_ids):

    r = []
    for id in client_ids:
        average = 0
        rows = df[df['client_id']==id]
        if not rows.empty:
            n = len(rows)
            total = rows['tran_amt_rur'].sum()
            average = total/n
        r.append(average)
    r = np.array(r)
    print('avg_trxn_amount',r.shape)
    return r

def process_txn_comment_1(df, client_ids):

    mp = {
        'Cash withdrawal through an ATM': 0,
        'Payment for goods and services': 1,
        'Payment by card (bank transfer)': 2 ,
        'Cash deposit by card': 3,
        'Return of goods / services': 4 ,
        'Cash withdrawal': 5,
        'Cashless transfer': 6
    }

    r = []
    for id in client_ids:
        count = [0]*7
        rows = df[df['client_id']==id]
        if not rows.empty:
            for comment in mp.keys():
                rows = rows[rows['txn_comment_1']==comment]
                sm = rows['tran_amt_rur'].sum()
                count[mp[comment]] = sm
        r.append(count)
    r = np.array(r)
    print('txn_comment_1',r.shape)
    return r
            


def load_x(df, client_ids):

    #one-to-many
    card_count = process_card_count(df, client_ids)
    avg_trxn_amount = process_avg_trxn_amount(df, client_ids)
    txn_comment_1 = process_txn_comment_1(df, client_ids)

    return np.column_stack((card_count, avg_trxn_amount, txn_comment_1))