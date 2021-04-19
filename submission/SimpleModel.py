from xgboost import XGBClassifier

class SimpleModel():
    def __init__(self):
        
        self.model = XGBClassifier()

    def fit(self, x, y, val_x, val_y):
        eval_set = [(val_x,val_y)]
        self.model.fit(x, y, early_stopping_rounds=10, eval_metric="logloss", eval_set=eval_set, verbose=True)

    def predict(self, x):
        return self.model.predict(x)
    
