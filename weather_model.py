# code       that       constructs and returns       WeatherModel
import psycopg2
conn = psycopg2.connect(host="localhost", port="5432", database="taras")


class WeatherModel:
    def __init__(self, id: int = 0, location: str | None = None, temperature: int | None = None):
      self.id = id
      self.location = location
      self.temperature = temperature

    @staticmethod
    def save(location: str, temperature: int):
      cur = conn.cursor()
      cur.execute('INSERT INTO weather (temperature, location) VALUES (%s, %s) RETURNING id', (temperature, location))
      new_id = cur.fetchone()[0]
      conn.commit()
      return new_id

    @staticmethod
    def load(id: int, location: str | None = None, temperature: int | None = None):
      cur = conn.cursor()
      cur.execute('Select * from weather where id = %s', (id,))
      record = cur.fetchone()
      return WeatherModel(*record)

    @staticmethod
    def update(id: int, location: str | None = None, temperature: int | None = None):
        cur = conn.cursor()
        rows_updated = 0
        cur.execute("UPDATE weather SET location = %s, temperature = %s WHERE id = %s RETURNING id", (location, temperature, id))
        updated_id = cur.fetchone()[0]
        conn.commit()
        return updated_id

    @staticmethod
    def delete_weather(id: int):
        #sql = 'DELETE FROM weather WHERE id = %s RETURNING id'
        cur = conn.cursor()
        cur.execute('DELETE FROM weather WHERE id = %s RETURNING id')
        deleted_id = cur.fetchone()[0]
        conn.commit()
        return deleted_id