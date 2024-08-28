import requests

from db import connect_to_db
from config import config

def get_country_info():
	cur, conn = connect_to_db()
	cur.execute("SELECT * FROM Countries;")
	data = {}
	for country in cur.fetchall():
		country_data = {}
		country_data["Name"] = country[1]
		country_data["Official Name"] = country[2]
		country_data["Population"] = country[3]
		country_data["Continent"] = country[4]
		country_data["Flag"] = country[5]
		data[country[0]] = country_data

	return data

def get_articles(country):
	cur, conn = connect_to_db()
	cur.execute("SELECT * FROM News WHERE country = %s;", (country.upper(),))

	articles = cur.fetchall()

	if len(articles) > 0:
		data = []

		for item in articles:
			article_data = {}
			article_data["Id"] = item[0]
			article_data["Title"] = item[1]
			article_data["Url"] = item[2]
			article_data["Clean Url"] = item[3]
			article_data["Country"] = item[4]
			data.append(article_data)
		return data
	
	else:
		url = config["covid_news_url"]

		querystring = {"q":"covid","lang":"en","country": country}

		headers = {
			"x-rapidapi-key": config["x_rapidapi_key"],
			"x-rapidapi-host": config["x_rapidapi_host"]
		}

		response = requests.get(url, headers=headers, params=querystring)

		data = response.json()

		if data["status"] == "ok":
			articles = data["articles"]
			result = []

			for item in articles:
				cur.execute("INSERT INTO News VALUES (%s, %s, %s, %s, %s);", (item["_id"], item["title"], item["link"], item["clean_url"], item["country"]))
				conn.commit()
				article_data = {}
				article_data["Id"] = item["_id"]
				article_data["Title"] = item["title"]
				article_data["Url"] = item["link"]
				article_data["Clean Url"] = item["clean_url"]
				article_data["Country"] = item["country"]
				result.append(article_data)
			return result
		return []