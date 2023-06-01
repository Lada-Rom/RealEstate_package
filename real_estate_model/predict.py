from pathlib import Path

import lightgbm as lgb
import numpy as np
import pandas as pd

from real_estate_model.config import Config, fetch_config_from_yaml

PACKAGE_ROOT = Path(__file__).resolve().parent


def load_model():
    config = Config(**fetch_config_from_yaml().data)
    MODEL_FILE_PATH = PACKAGE_ROOT / config.predict_model
    model = lgb.Booster(model_file=MODEL_FILE_PATH)
    print(MODEL_FILE_PATH)
    return model


def predict_raw(model, predictors_values):
    config = Config(**fetch_config_from_yaml().data)
    data = pd.DataFrame([predictors_values], columns=config.predictors)
    case = pd.DataFrame(data=data, index=[0])
    prediction = model.predict(case)
    print(type(prediction[0]))
    return np.float64("{:.2f}".format(prediction[0] / 150000 * 10**18))


# geo_lat float
# geo_lon float
# Region uint categoric
#   Region of Russia. There are 85 subjects in the country in total.
# level uint
# levels uint
# rooms uint
# area float
# object_type uint categoric
#   1 = new build
#   2 = secondary build
def predict(predictors_values):
    model = load_model()
    prediction = predict_raw(model, predictors_values)
    return prediction


if __name__ == "__main__":
    price = predict([80.805808, 30.376141, 8, 10, 3, 82.6, 2])
    print(f"{price} Wei")
