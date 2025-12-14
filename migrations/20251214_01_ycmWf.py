import os
import urllib.parse
import logging
from argparse import ArgumentParser

from yoyo import read_migrations
from yoyo import get_backend
#from yoyo import step
from dotenv import load_dotenv

#steps = [
   #step(
     #  "CREATE TABLE weather (id INT, bar VARCHAR(20), PRIMARY KEY (id))",
     #  "DROP TABLE foo"
  # )
#]

load_dotenv()

host     = os.environ["PG_HOSTNAME"]
port     = os.environ["PG_PORT"]
user     = os.environ["PG_USERNAME"]
password = os.environ["PG_PASSWORD"]
database = os.environ["PG_DATABASE"]

parser = ArgumentParser(description="Runs migrations")
parser.add_argument("-f", "--file", help="File with migrations", metavar="FILE", default="migrations")
args = parser.parse_args()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

backend    = get_backend(f"postgres://{user}:{urllib.parse.quote_plus(password)}@{host}:{port}/{database}")
migrations = read_migrations(args.file)

logger.info("Applying database migrations...")
with backend.lock():
    backend.apply_migrations(backend.to_apply(migrations))

logger.info("Database migration completed")