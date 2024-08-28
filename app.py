from flask import Flask, jsonify, render_template

from config import config
from helpers.functions import get_articles, get_country_info

app = Flask(__name__)

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


if __name__ == "__main__":
	app.run(debug=False)