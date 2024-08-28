import os
from dotenv import load_dotenv

load_dotenv()

config = {
	"db_url": os.environ["DB_URL"],
	"debug": os.environ["DEBUG"],
	"country_info_url": os.environ["COUNTRY_INFO_URL"],
	"covid_news_url": os.environ["COVID_NEWS_URL"],
	"x_rapidapi_key": os.environ["X_RAPIDAPI_KEY"],
	"x_rapidapi_host": os.environ["X_RAPIDAPI_HOST"],
}