from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from weather_model import WeatherModel

app = FastAPI()


#class Weather(BaseModel):
    #timestamp: datetime
    #dimensions: tuple[int, int]

@app.get("/weather")
def get_weather():
    weather = WeatherModel()
    return weather

@app.post("/weather")
def create_item (weather: WeatherModel):
    weather.feeling = str
    weather.humidity = int
    return weather

@app.put("/weather/{item_id}")
def humidity_edit (item_id: int, weather: WeatherModel):
    weather.humidity = 1
    return weather

@app.delete("/weather")
def delete_humidity (weather: WeatherModel):
    weather.humidity = None
    return weather