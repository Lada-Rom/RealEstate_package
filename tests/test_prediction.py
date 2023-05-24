import numpy as np

from real_estate_model.predict import predict


def test_predict():
    pred_input = [80.805808, 30.376141, 2661, 8, 10, 3, 82.6, 1]
    prediction = predict(pred_input)

    print()
    assert type(prediction) is np.float64
    print("type test passed")
    assert prediction > 0
    print("value test passed")
