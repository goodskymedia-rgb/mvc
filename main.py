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

@app.post("/weather/")
def create_item (weather: Weather):
    weather.feeling = "feeling good"
    weather.humidity = 4
    return weather

@app.put("/weather/{item_id}")
def humidity_edit (item_id: int, weather: Weather):
    weather.humidity = 1
    return weather

@app.delete("/weather")
def delete_humidity (weather: Weather):
    weather.humidity = None
    return weather