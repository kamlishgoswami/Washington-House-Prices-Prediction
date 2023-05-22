from fastapi import FastAPI, Request, Body
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import util

app = FastAPI()

# Configure CORS settings
origins = [
    "null",  # Update with the appropriate origin for your HTML page
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)

@app.get('/get_location_names')
def get_location_names():
    locations = util.get_location_names()
    return {'locations': locations}

@app.post('/predict_home_price')
async def predict_home_price(request: Request, bedrooms: int = Body(...), bathrooms: int = Body(...), sqft_living: int = Body(...), sqft_lot: int = Body(...), floors: int = Body(...), waterfront: int = Body(...), condition: int = Body(...), location: str = Body(...)):
    estimated_price = util.get_estimated_price(bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, condition, location)
    return {'estimated_price': estimated_price}

@app.options('/predict_home_price')
async def options_predict_home_price(request: Request):
    allowed_methods = ["POST", "OPTIONS"]
    response_headers = {"Allow": ", ".join(allowed_methods)}
    return JSONResponse(status_code=200, headers=response_headers)

@app.on_event("startup")
async def startup_event():
    print("Starting Python FastAPI Server For Home Price Prediction...")
    util.load_saved_artifacts()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
