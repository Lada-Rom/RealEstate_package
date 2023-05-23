from config import Config, fetch_config_from_yaml
from pandas import read_csv
import lightgbm as lgb

import calendar
import time

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


def calc_metrics(actual, pred, suffix):
    #rmse = sqrt(mean_squared_error(actual, pred))
    r2 = r2_score(actual,pred)
    #print(f'{suffix} rmse: {rmse}')
    print(f'{suffix} R2: {r2}')

def train() -> None:
    # getting train params
    config = Config(**fetch_config_from_yaml().data)

    # read training data
    data = read_csv(config.dataset)

    # process data
    price=data[data['price'] <= 0].index
    data.drop(price, inplace=True)

    rooms=data[data['rooms']<= 0].index
    data.drop(rooms, inplace=True)

    price_high=data[data['price']>=20.000000e+06].index
    data.drop(price_high, inplace=True)

    # drop variables to drop
    labels_to_drop = config.variables_to_drop
    labels_to_drop.append('price')
    X = data.drop(labels=labels_to_drop, axis=1)
    Y = data['price']

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(X, Y,
        test_size=config.train_size,
        random_state=config.random_state,
    )

    # fit model
    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_eval = lgb.Dataset(X_test, y_test)
    params={'metric': config.metric}
    model = lgb.train(params,
                    lgb_train,
                    valid_sets=lgb_eval,
                    num_boost_round=config.num_boost_round,
                    early_stopping_rounds=config.early_stopping_rounds,
                    verbose_eval=config.verbose_eval)

    # make predictions for train set
    train_predicted = model.predict(X_train)
    train_rmse = calc_metrics(y_train, train_predicted, "train")

    # make predictions for test set
    test_predicted = model.predict(X_test)
    test_rmse = calc_metrics(y_test, test_predicted, "test")
    print()

    # persist trained model
    timestamp = calendar.timegm(time.gmtime())
    model_filename = config.trained_model_path\
        + "lightgbm_" + str(timestamp) + ".txt"
    model.save_model(model_filename)


if __name__ == "__main__":
    train()
