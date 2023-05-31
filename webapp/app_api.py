from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn

from pydantic import BaseModel
from real_estate_model.predict import predict_raw, load_model
from real_estate_model.train import train
from real_estate_model.config import set_config_field


class NnInput(BaseModel):
    geo_lat: float
    geo_lon: float
    level: int
    levels: int
    rooms: int
    area: float
    object_type: int

    class Config:
        schema_extra = {
            "example": {
                "geo_lat": 55.683807,
                "geo_lon": 37.297405,
                "level": 5,
                "levels": 24,
                "rooms": 2,
                "area": 69.1,
                "object_type": 2
            }
        }

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
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>RealEstate Super DApp</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )
    return HTMLResponse(content=body)

@api_router.post("/predict", status_code=200)
async def predict_method(input: NnInput):
    model = load_model()
    nn_input = [input.geo_lat, input.geo_lon, input.level,
                input.levels, input.rooms, input.area, input.object_type]
    res = predict_raw(model, nn_input)
    return res

@api_router.post("/train", status_code=200)
async def train_method():
    abs_filepath, rel_filepath, r2_train, r2_test = train()
    res_dict = {
        'abs_filepath' : abs_filepath,
        'rel_filepath' : rel_filepath,
        'R2_train': r2_train,
        'R2_test': r2_test
    }
    return res_dict

@api_router.post("/change_model", status_code=200)
async def change_method(filepath: str):
    set_config_field("predict_model", filepath)
    return "success!"


if __name__ == '__main__':
    uvicorn.run(api_router, port=8000, host='0.0.0.0')
