from fastapi import FastAPI
from pydantic import BaseModel

from weather_model import WeatherModel

app = FastAPI()

class Weather(BaseModel):
    location: str
    temperature: int

@app.get("/weather")
def get_weather(id: int):
    weather = WeatherModel().load(id)
    return Weather(location = weather.location, temperature = weather.temperature)

@app.post("/weather")
def create_item (weather: Weather):
    new_id = WeatherModel().save(weather.location, weather.temperature)
    #weather = WeatherModel().save(weather.location, weather.temperature)
    return weather

@app.put("/weather/{id}")
def temperature_edit(id: int, weather: Weather):
    WeatherModel().update(id, temperature=weather.temperature, location=weather.location)
    return {"status": "temperature was updated"}

@app.delete("/weather/{id}")
def row_delete(id: int, weather: Weather):
    WeatherModel().delete_weather(id)
    return {"status": "item was deleted"}