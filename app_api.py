from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from loguru import logger
from pydantic import BaseModel
from predict import predict
import pandas as pd
import json
import uvicorn

class NnInput(BaseModel):
    geo_lat: float
    geo_lon: float
    region: int
    level: int
    levels: int
    rooms: int
    area: float
    object_type: int

api_router = FastAPI()

origins = ["*"]
api_router.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api_router.get("/", status_code=200)
def hello():
    return "HALLo"

@api_router.post("/predict", status_code=200)
async def cool_method(input: NnInput):
    #return input
    #logger.info(f"Making prediction on inputs: {input_data.inputs}")
    #print(req_info)
    res = predict(input.geo_lat, input.geo_lon, input.region, input.level,
                  input.levels, input.rooms, input.area, input.object_type)

    #if results["errors"] is not None:
    #    logger.warning(f"Prediction validation error: {results.get('errors')}")
    #    raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    #logger.info(f"Prediction result class: {results.get('preds')}")
    #logger.info(f"Prediction result probability: {results.get('probs')}")

    return res

if __name__ == '__main__':
    uvicorn.run(api_router, port=8000, host='0.0.0.0')