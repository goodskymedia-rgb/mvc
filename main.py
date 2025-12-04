from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

@app.get("/weather")
def get_weather():
    class Weather(BaseModel):
        timestamp: datetime
        dimensions: tuple[int, int]
    weather = Weather(timestamp=datetime.strptime("2025-12-03", "%Y-%m-%d"),dimensions=(2, 3))
    #weather = {"timestamp": 1, "temperature": {"value": 13, "unit": "celcius"}, "humidity": 4, "uv-index": 4}
    return weather

@app.put("/weather")
def root():
    return {}

@app.delete("/weather")
def root():
    return {}

@app.post("/weather")
def root():
    return {}