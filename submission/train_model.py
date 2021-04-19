import configparser
import pathlib as path
import logging

import numpy as np
import pandas as pd
import joblib

from SimpleModel import SimpleModel
from utils import split
from process import load_data

logging.basicConfig(format='%(asctime)s %(message)s', filename='training.log', level=logging.DEBUG)

def main(cfg):
    
    # parse config
    DATA_FOLDER = path.Path(cfg["DATA"]["DatasetPath"])
    MODEL_PATH = path.Path(cfg["MODEL"]["FilePath"])
    # do something with data
    #X = pd.read_csv(f'{DATA_FOLDER}/{cfg["DATA"]["UsersFile"]}')

    x,y = load_data('train', cfg)
    train_x, val_x = split(x)
    train_y, val_y = split(y)

    model = SimpleModel()

    model.fit(train_x, train_y, val_x, val_y)

    joblib.dump(model, MODEL_PATH)
    logging.info("model was trained")


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("./config.ini")
    main(cfg=config)
