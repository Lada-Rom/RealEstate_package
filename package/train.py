import calendar
import time
from pathlib import Path

import lightgbm as lgb
from pandas import read_csv
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from package.config import Config, fetch_config_from_yaml


def calc_metrics(actual, pred, suffix):
    # rmse = sqrt(mean_squared_error(actual, pred))
    r2 = r2_score(actual, pred)
    # print(f'{suffix} rmse: {rmse}')
    print(f"{suffix} R2: {r2}")


def train() -> None:
    # getting train params
    config = Config(**fetch_config_from_yaml().data)

    # read training data
    PACKAGE_ROOT = Path(__file__).resolve().parent
    DATASET_FILE_PATH = PACKAGE_ROOT / config.dataset
    data = read_csv(DATASET_FILE_PATH)

    # process data
    price = data[data["price"] <= 0].index
    data.drop(price, inplace=True)

    rooms = data[data["rooms"] <= 0].index
    data.drop(rooms, inplace=True)

    price_high = data[data["price"] >= 20.000000e06].index
    data.drop(price_high, inplace=True)

    # drop variables to drop
    labels_to_drop = config.variables_to_drop
    labels_to_drop.append("price")
    X = data.drop(labels=labels_to_drop, axis=1)
    Y = data["price"]

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=config.train_size, random_state=config.random_state
    )

    # fit model
    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_eval = lgb.Dataset(X_test, y_test)
    params = {"metric": config.metric}
    model = lgb.train(
        params,
        lgb_train,
        valid_sets=lgb_eval,
        num_boost_round=config.num_boost_round,
        early_stopping_rounds=config.early_stopping_rounds,
        verbose_eval=config.verbose_eval,
    )

    # make predictions for train set
    model.predict(X_train)

    # make predictions for test set
    model.predict(X_test)
    print()

    # persist trained model
    timestamp = calendar.timegm(time.gmtime())
    model_filename = config.trained_model_path + "lightgbm_" + str(timestamp) + ".txt"
    TRAINED_FILE_PATH = PACKAGE_ROOT / model_filename
    model.save_model(TRAINED_FILE_PATH)


if __name__ == "__main__":
    train()
