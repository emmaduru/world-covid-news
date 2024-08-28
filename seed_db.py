from scripts.create_tables import create_tables
from scripts.save_country_info import save_country_info

def seed_db():
	save_country_info()
	create_tables()

seed_db()