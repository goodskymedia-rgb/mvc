import psycopg2
#connection = psycopg2.connect(host="localhost", port="5432", database="taras")

class WeatherModel:
  def __init__(self):
      id = int
      location = str
      temperature = int

  def save(self, temp: int, location: str, temperature: int) -> bool:
      conn = psycopg2.connect(host="localhost", port="5432", database="taras")
      cur = conn.cursor()
      cur.execute('INSERT INTO weather (temp, location) VALUES (%s, %s)', (temp, location))
      return True

  def load(self, id: int, location: str, temperature: int) -> WeatherModel:
      conn = psycopg2.connect(host="localhost", port="5432", database="taras")
      cur = conn.cursor()
      cur.execute('Select * from weather where id = %s', (id))

      # code       that       constructs and returns       WeatherModel
