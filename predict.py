import lightgbm as lgb
import pandas as pd

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
#   2 = new build
def predict(geo_lat, geo_lon, region, level, levels, rooms, area, object_type):
    model = lgb.Booster(model_file = "lgb_model.txt")
    
    data = {'geo_lat': geo_lat, 'geo_lon': geo_lon, 'region': region, 'level': level,
            'levels': levels, 'rooms': rooms, 'area': area, 'object_type': object_type}
    case = pd.DataFrame(data=data, index=[0])
    prediction = model.predict(case)
    return prediction[0]

if __name__ == '__main__':
    price = predict(80.805808, 30.376141, 2661, 8, 10, 3, 82.6, 1)
    print(f"{price:.2f} Wei")