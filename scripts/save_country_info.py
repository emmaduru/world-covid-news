import json
from urllib.request import urlopen
import pandas as pd
from config import config

def save_country_info():
	url = config["country_info_url"]
	response = urlopen(url)

	if response.getcode() == 200:
		# Parse data into JSON
		data = json.loads(response.read().decode("utf-8"))
		countries = []
		for country in data:
			country_data = {}
			country_data["Country"] = country["name"]["common"]
			country_data["Official Name"] = country["name"]["official"]
			country_data["Population"] = country["population"]
			country_data["Continent"] = country["continents"][0]
			country_data["Flag"] = country["flags"]["png"]
			country_data["ISO 2 Code"] = country["cca2"]

			countries.append(country_data)

		df = pd.DataFrame(countries).set_index("Country")
		df.to_csv("scripts/data/countries_info.csv")
	else:
		print("Error fetching data")