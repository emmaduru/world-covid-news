from flask import Flask, jsonify, render_template
from flask_apscheduler import APScheduler

from config import config
from helpers.functions import get_articles, get_country_info
from db import connect_to_db

app = Flask(__name__)
scheduler = APScheduler()

@app.route("/countries", methods=["GET"])
def home():
	country_info = get_country_info()
	return jsonify(country_info)

@app.route("/news/<iso_code>", methods=["GET"])
def get_top_headlines(iso_code):
	articles = get_articles(iso_code)
	return jsonify(articles)

@app.route("/", methods=["GET"])
def get_map():
	return render_template("home.html")


# Cron job to delete all rows from the News table at midnight
@scheduler.task("cron", id="clear_news_table", hour=0, minute=0)
def clear_news_table():
	cur, conn = connect_to_db()
	cur.execute("DELETE FROM News;")
	cur.close()
	print("News Table cleared.")
	

if __name__ == "__main__":
	scheduler.init_app(app)
	scheduler.start()
	app.run(debug=False)