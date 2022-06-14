# Load Python modules for object serialization
import pickle

# Initialize FastAPI object and import relevant modules
from typing import Union, Optional
from fastapi import FastAPI, Path, Query

# Load Body Parameters
from parameters.body_params import HouseFeatures

# Load the model
filename = "saved_models/rf_dep.pkl"
rf_model = pickle.load(open(filename, "rb"))

# Initialize the app
app = FastAPI()

# Initialize results for sending a response via GET request
results = {}


# Define the API route to ACCESS the parameters and perform predictions. 'POST' request
@app.post("/get-House-Fs")
def get_House_fs(*, request: HouseFeatures):
    overallQuality = request.overallQuality
    if overallQuality is None:
        overallQuality = 1
    elif overallQuality == "Very Poor":
        overallQuality = 1
    elif overallQuality == "Poor":
        overallQuality = 2
    elif overallQuality == "Fair":
        overallQuality = 3
    elif overallQuality == "Below Average":
        overallQuality = 4
    elif overallQuality == "Average":
        overallQuality = 5
    elif overallQuality == "Above Average":
        overallQuality = 6
    elif overallQuality == "Good":
        overallQuality = 7
    elif overallQuality == "Very Good":
        overallQuality = 8
    elif overallQuality == "Excellent":
        overallQuality = 9
    elif overallQuality == "Very Excellent":
        overallQuality = 10

    results.update({"Overall Quality": overallQuality})

    livingRoomArea = request.livingRoomArea
    if livingRoomArea is None:
        livingRoomArea = 334
    else:
        livingRoomArea = int(livingRoomArea)

    results.update({"Living Room Area": livingRoomArea})

    basementArea = request.basementArea
    if basementArea is None:
        basementArea = 0
    else:
        basementArea = int(basementArea)

    results.update({"Basement Area": basementArea})

    firstFloorArea = request.firstFloorArea
    if firstFloorArea is None:
        firstFloorArea = 334
    else:
        firstFloorArea = int(firstFloorArea)

    results.update({"First Floor Total Area": firstFloorArea})

    firstFlrConsArea = request.firstFlrConsArea
    if firstFlrConsArea is None:
        firstFlrConsArea = 0
    else:
        firstFlrConsArea = int(firstFlrConsArea)

    results.update({"Constructed first floor area": firstFlrConsArea})

    secondFlrTotArea = request.secondFlrTotArea
    if secondFlrTotArea is None:
        secondFlrTotArea = 0
    else:
        secondFlrTotArea = int(secondFlrTotArea)

    results.update({"Total second floor area": secondFlrTotArea})

    lotArea = request.lotArea
    if lotArea is None:
        lotArea = 1300
    else:
        lotArea = int(lotArea)

    results.update({"Lot Area": lotArea})

    yrBlt = request.yrBlt
    if yrBlt is None:
        yrBlt = 1872
    else:
        yrBlt = int(yrBlt)

    results.update({"Year of house built": yrBlt})

    bathAboveGrade = request.bathAboveGrade
    if bathAboveGrade is None:
        bathAboveGrade = 0
    else:
        bathAboveGrade = int(bathAboveGrade)

    results.update({"No. of bathrooms above grade": bathAboveGrade})

    yrGarageBlt = request.yrGarageBlt
    if yrGarageBlt is None:
        yrGarageBlt = 1895
    else:
        yrGarageBlt = int(yrGarageBlt)

    results.update({"Year of garage built": yrGarageBlt})

    porchArea = request.porchArea
    if porchArea is None:
        porchArea = 0
    else:
        porchArea = int(porchArea)

    results.update({"Total Porch Area": porchArea})

    garageArea = request.garageArea
    if garageArea is None:
        garageArea = 0
    else:
        garageArea = int(garageArea)

    results.update({"Total Garage Area": garageArea})

    garageCarCap = request.garageCarCap
    if garageCarCap is None:
        garageCarCap = 0
    else:
        garageCarCap = int(garageCarCap)

    results.update({"Total Garage Car Capacity": garageCarCap})

    overallCond = request.overallCond
    if overallCond is None:
        overallCond = 1
    elif overallCond == "Very Poor":
        overallCond = 1
    elif overallCond == "Poor":
        overallCond = 2
    elif overallCond == "Fair":
        overallCond = 3
    elif overallCond == "Below Average":
        overallCond = 4
    elif overallCond == "Average":
        overallCond = 5
    elif overallCond == "Above Average":
        overallCond = 6
    elif overallCond == "Good":
        overallCond = 7
    elif overallCond == "Very Good":
        overallCond = 8
    elif overallCond == "Excellent":
        overallCond = 9
    elif overallCond == "Very Excellent":
        overallCond = 10

    results.update({"Overall Condition Rating ": overallCond})

    # Perform predictions
    preds = rf_model.predict([[overallQuality, livingRoomArea, basementArea, firstFloorArea, firstFlrConsArea,
                               secondFlrTotArea, lotArea, yrBlt, bathAboveGrade, yrGarageBlt, porchArea, garageArea,
                               garageCarCap, overallCond]])
    preds_final = round(preds[0], 2)

    return {"Predictions": preds_final}
