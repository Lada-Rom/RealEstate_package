import lightgbm as lgb
import pandas as pd

# geo_lat float
# geo_lon float
# region uint categoric
# level uint
# levels uint
# rooms uint
# area float
# object_type uint categoric
def predict(geo_lat, geo_lon, region, level, levels, rooms, area, object_type):
    model = lgb.Booster(model_file = "lgb_model.txt")
    
    data = {'geo_lat': geo_lat, 'geo_lon': geo_lon, 'region': region, 'level': level,
            'levels': levels, 'rooms': rooms, 'area': area, 'object_type': object_type}
    case = pd.DataFrame(data=data, index=[0])
    prediction = model.predict(case)
    return prediction[0]
    
 predict(59.805808, 30.376141, 2661, 8, 10, 3, 82.6, 1)