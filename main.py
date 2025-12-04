from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class Weather(BaseModel):
    timestamp: datetime
    dimensions: tuple[int, int]

@app.get("/weather")
def get_weather():
    weather = Weather(timestamp=datetime.strptime("2025-12-03", "%Y-%m-%d"),dimensions=(2, 3))
    #weather = {"timestamp": 1, "temperature": {"value": 13, "unit": "celcius"}, "humidity": 4, "uv-index": 4}
    return weather

@app.put("/weather")
def root():
    return {}

@app.delete("/weather")
def root():
    return {}

@app.post("/items/")
def create_item (weather: Weather):
    feeling = "feeling good"
    return feeling