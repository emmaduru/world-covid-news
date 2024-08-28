import psycopg2
from config import config

def connect_to_db():
	try:
		conn = psycopg2.connect(config["db_url"])
		cur = conn.cursor()
		return cur, conn

	except psycopg2.Error as error:
		print(error)
		return None