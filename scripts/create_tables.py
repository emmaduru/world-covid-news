from db import connect_to_db
import csv


def create_tables():
	
	cur, conn = connect_to_db()

	sql = """
	CREATE TABLE IF NOT EXISTS Countries (
		iso_code VARCHAR PRIMARY KEY,
		name VARCHAR (255),
		official_name VARCHAR (255) UNIQUE,
		population INTEGER,
		continent VARCHAR(255),
		flag VARCHAR(255)
	);
	"""
	cur.execute(sql)
	conn.commit()

	sql = """
	
	CREATE TABLE IF NOT EXISTS News (
		id VARCHAR PRIMARY KEY,
		title VARCHAR (255),
		url VARCHAR (255),
		clean_url VARCHAR (255),
		country VARCHAR(255)
	);
	"""
	cur.execute(sql)
	conn.commit()

	with open("scripts/data/countries_info.csv", "r") as file:
		csv_reader = csv.DictReader(file, delimiter=",")
		for row in csv_reader:
			cur.execute("SELECT * FROM Countries WHERE iso_code = %s", (row["ISO 2 Code"],))
			if len(cur.fetchall()) == 0:
				cur.execute("INSERT INTO Countries VALUES (%s,%s,%s,%s,%s,%s);", (row["ISO 2 Code"], row["Country"], row["Official Name"], row["Population"], row["Continent"], row["Flag"]))
				conn.commit()

	cur.close()


