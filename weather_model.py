import psycopg2
connection = psycopg2.connect(host="localhost", port="5432", database="taras")

class WeatherModel:
  def __init__(self, id: int = 0, location: str | None = None, temperature: int | None = None):
      self.id = id
      self.location = location
      self.temperature = temperature

  @staticmethod
  def save(location: str, temperature: int) -> bool:
      conn = psycopg2.connect(host="localhost", port="5432", database="taras")
      cur = conn.cursor()
      cur.execute('INSERT INTO weather (temp, location) VALUES (%s, %s)', (temp, location))
      return True

  @staticmethod
  def load(id: int, location: str | None = None, temperature: int | None = None) -> WeatherModel:
      conn = psycopg2.connect(host="localhost", port="5432", database="taras")
      cur = conn.cursor()
      cur.execute('Select * from weather where id = %s', (id))

      # code       that       constructs and returns       WeatherModel
