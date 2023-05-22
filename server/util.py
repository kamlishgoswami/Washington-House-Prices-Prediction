import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,condition,location):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bedrooms
    x[1] = bathrooms
    x[2] = sqft_living
    x[3] = sqft_lot
    x[4] = floors
    x[5] = waterfront
    x[6] = condition
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[7:]  # first 7 columns are "bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors", "waterfront", "condition", 

    global __model
    if __model is None:
        with open('./artifacts/washington_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns
