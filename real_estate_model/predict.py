from pathlib import Path

import lightgbm as lgb
import pandas as pd

from real_estate_model.config import Config, fetch_config_from_yaml

config = Config(**fetch_config_from_yaml().data)
PACKAGE_ROOT = Path(__file__).resolve().parent
MODEL_FILE_PATH = PACKAGE_ROOT / config.predict_model
model = lgb.Booster(model_file=MODEL_FILE_PATH)


# geo_lat float
# geo_lon float
# Region uint categoric
#   Region of Russia. There are 85 subjects in the country in total.
# level uint
# levels uint
# rooms uint
# area float
# object_type uint categoric
#   1 = secondary build
#   11 = new build
def predict(predictors_values):
    data = pd.DataFrame([predictors_values], columns=config.predictors)
    case = pd.DataFrame(data=data, index=[0])
    prediction = model.predict(case)
    return prediction[0]


if __name__ == "__main__":
    price = predict([80.805808, 30.376141, 2661, 8, 10, 3, 82.6, 1])
    print(f"{price:.2f} Rub")
