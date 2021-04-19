import configparser
import pathlib as path

import numpy as np
import pandas as pd
import joblib

from SimpleModel import SimpleModel
from process import load_data

def main(cfg):

    # parse config
    DATA_FOLDER = path.Path(cfg["DATA"]["DatasetPath"])
    USER_ID = cfg["COLUMNS"]["USER_ID"]
    PREDICTION = cfg["COLUMNS"]["PREDICTION"]
    MODEL_PATH = path.Path(cfg["MODEL"]["FilePath"])
    SUBMISSION_FILE = path.Path(cfg["SUBMISSION"]["FilePath"])
    # do something with data
    #X = pd.read_csv(f'{DATA_FOLDER}/{cfg["DATA"]["UsersFile"]}')

    x, client_ids = load_data('test', cfg)

    model = joblib.load(MODEL_PATH)

    preds = model.predict(x)
    preds = np.round(preds.flatten()).astype(int)

    sub = pd.DataFrame.from_dict(
        {
            'client_id': client_ids.tolist(),
            'target': preds.tolist()
        }
    )
    sub.to_csv(SUBMISSION_FILE, index=False)

    #submission = X[[USER_ID]].copy()
    #submission[PREDICTION] = np.random.choice([0, 1], len(submission))
    #submission[PREDICTION] = np.round(model.predict(X[['feature_1']])).astype(int)
    #submission.to_csv(SUBMISSION_FILE, index=False)


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("./config.ini")
    main(cfg=config)
